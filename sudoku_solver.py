class sudokusolver:
	_puzzle		= []
	_original 	= []

	def __init__(self, puzzle: list[int]) -> None:
		if (not isinstance(puzzle, list)):
			raise TypeError("puzzle must be a list of integers")

		if (len(puzzle) != 81):
			raise ValueError(f"puzzle must have exactly 81 elements, got {len(puzzle)}")

		if (not all(type(val) is int and 0 <= val <= 9 for val in puzzle)):
			raise ValueError("puzzle elements must be integers from 0 to 9")

		# Copy so mutating the puzzle during solving doesn't surprise the caller
		self._puzzle = puzzle.copy()
	
	def print_puzzle(self) -> None:
		for r_idx in range(9):
			if r_idx % 3 == 0 and r_idx != 0:
				print("-" * 21)
			row = self._puzzle[r_idx * 9 : (r_idx + 1) * 9]
			cells = [str(v) if v != 0 else "-" for v in row]
			print(f"{' '.join(cells[0:3])} | {' '.join(cells[3:6])} | {' '.join(cells[6:9])}")

	@staticmethod
	def get_row_num(index: int) -> int:
		return index // 9

	@staticmethod
	def get_col_num(index: int) -> int:
		return index % 9

	def get_block_num(self, index: int) -> int:
		row_num = self.get_row_num(index)
		col_num = self.get_col_num(index)

		return ((row_num // 3) * 3) + (col_num // 3)

	def row_valid(self, index: int, value: int) -> bool:
		row_num = self.get_row_num(index)
		start 	= row_num * 9
		end 	= start + 9

		# print(f"row:{row_num} ", end="")
		for i in range(start, end):
			# print(f"r[{i}]={puzzle[i]} ", end="")
			if (self._puzzle[i] == value):
				return False
		# print()

		return True

	def col_valid(self, index: int, value: int) -> bool:
		col_num = self.get_col_num(index)

		# print(f"col:{col_num} ", end="")
		for i in range(9):
			col_index = (i * 9) + col_num
			# print(f"c[{col_index}]={puzzle[col_index]} ", end="")
			if (self._puzzle[col_index] == value):
				return False
		# print()

		return True

	def block_valid(self, index: int, value: int) -> bool:
		row_num_block	= self.get_row_num(index) // 3
		col_num_block	= self.get_col_num(index) // 3


		start = ((row_num_block * 3) * 9) + (col_num_block * 3)

		block_num = self.get_block_num(index)
		# print(f"blk:{block_num} (start:{start}) ", end="")

		for i in range(9):
			row		= i % 3
			col 	= i // 3

			block_index	= (start + row) + (col * 9)
			# print(f"b[{block_index}]={puzzle[block_index]} ", end="")
			if (self._puzzle[block_index] == value):
				return False
		# print()

		return True

	def value_is_valid(self, index: int, value: int) -> bool:
		return (
			self._puzzle[index] == 0
			and self.row_valid(index, value)
			and self.col_valid(index, value)
			and self.block_valid(index, value)
		)

	def guess_value(self, index: int, start_val) -> int:
		print(f"Guessing index {index}. ", end="")
		for i in range(start_val, 10):
			print(f"{i}...", end="")
			if (self.value_is_valid(index, i)):
				return i

	def solve(self):
		self._original = self._puzzle.copy()
		index 	= 0
		solved	= False
		regress = False
		while (not solved):
			og 		= self._original[index]
			value 	= self._puzzle[index]

			# Determine if we need to make a guess or just proceed with the original value
			if (og > 0):
				# Proceed with the original value
				value = og
			elif (value == 0):
				value = self.guess_value(index, 1)

				if (value == None):
					print("NEED TO REGRESS")
					self._puzzle[index] = 0
					regress = True
					self.print_puzzle()

			else:
				self._puzzle[index] = 0
				value = self.guess_value(index, value + 1)
				if (value == None):
					print("KEEP REGRESSING")
					regress = True
					self.print_puzzle()
				else:
					regress = False

			if (regress):
				index -= 1
				if (index < 0):
					print("UNSOLVABLE")
					return

			else:
				print(f"value = {value}")
				self._puzzle[index] = value
				# print(self._puzzle)
				index += 1

				if (index > 80):
					solved = True

sample1 = [
    5, 0, 8, 0, 0, 0, 0, 6, 0,
    0, 4, 2, 0, 0, 8, 0, 0, 3,
    6, 0, 3, 0, 4, 9, 0, 0, 7,
    8, 0, 9, 0, 3, 0, 0, 0, 0,
    3, 7, 0, 2, 0, 1, 0, 4, 8,
    0, 0, 0, 0, 8, 0, 3, 0, 2,
    2, 0, 0, 1, 5, 0, 4, 0, 9,
    1, 0, 0, 4, 0, 0, 2, 5, 0,
    0, 5, 0, 0, 0, 0, 7, 0, 1,
]

# MAIN
def main():
	solver = sudokusolver(sample1)
	solver.print_puzzle()

	solver.solve()
	# print(solver.guess_value(13, 2))
	solver.print_puzzle()

if __name__ == "__main__":
    main()