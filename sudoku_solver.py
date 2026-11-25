import time

class sudokusolver:
	_puzzle		= []
	_original 	= []
	_keep_stats	= False
	_statistics = {}

	def __init__(self, puzzle: list[int], keep_stats: bool) -> None:
		"""
		Goal here is to ALWAYS instantiate with a list of integers that is 81 values long and contains ONLY 0-9

		Args:
			puzzle (list[int]): _description_

		Raises:
			TypeError: puzzle is not a list type
			ValueError: puzzle is not 81 elements long
			ValueError: puzzle values are not between 0-9
		"""
		if (not isinstance(puzzle, list)):
			raise TypeError("puzzle must be a list of integers")

		if (len(puzzle) != 81):
			raise ValueError(f"puzzle must have exactly 81 elements, got {len(puzzle)}")

		if (not all(type(val) is int and 0 <= val <= 9 for val in puzzle)):
			raise ValueError("puzzle elements must be integers from 0 to 9")

		self._keep_stats = keep_stats

		# Copy so mutating the puzzle during solving doesn't surprise the caller
		self._puzzle = puzzle.copy()

	@staticmethod
	def get_row_num(index: int) -> int:
		"""
		Calculate the row number (0-8) from the index (0-80)

		Args:
			index (int): Index of the puzzle

		Returns:
			int: row number
		"""
		return index // 9

	@staticmethod
	def get_col_num(index: int) -> int:
		"""
		Calculate the column number (0-8) from the index (0-80)

		Args:
			index (int): Index of the puzzle

		Returns:
			int: column number
		"""
		return index % 9

	def get_block_num(self, index: int) -> int:
		"""
		Determine the block number from the index (0-80). Blocks are:
		0 1 2
		3 4 5
		6 7 8

		Args:
			index (int): Index of the puzzle

		Returns:
			int: block number
		"""
		row_num = self.get_row_num(index)
		col_num = self.get_col_num(index)

		return ((row_num // 3) * 3) + (col_num // 3)

	def row_valid(self, index: int, value: int) -> bool:
		"""
		Determine if a given value is acceptable in the given index with respect to the row.

		Args:
			index (int): Index of the puzzle
			value (int): value to be set at that index - need to verify

		Returns:
			bool: valid or not
		"""
		# Determine the row number to know what index the row starts on
		row_num = self.get_row_num(index)
		start 	= row_num * 9
		end 	= start + 9

		# print(f"row:{row_num} ", end="")
		# Iterate over from start of the row till end
		for i in range(start, end):
			# print(f"r[{i}]={puzzle[i]} ", end="")
			if (self._puzzle[i] == value):
				return False
		# print()

		return True

	def col_valid(self, index: int, value: int) -> bool:
		"""
		Determine if a value is valid for the column it is in

		Args:
			index (int): Index of the puzzle
			value (int): value desired to be put there

		Returns:
			bool: valid or not
		"""
		# When you have the first column number it gets easier
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
		"""
		Determine if a value is valid for the block it is in

		Args:
			index (int): Index of the puzzle
			value (int): value to put in that index

		Returns:
			bool: valid or not
		"""
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
		"""
		The heart of the sudoku solving. Can this value go here? Only if it is valid in 
		its row, col, and block. Not to mention there was not already a value there

		Args:
			index (int): Index of the puzzle
			value (int): value to put in that index

		Returns:
			bool: _description_
		"""
		return (
			self._puzzle[index] == 0
			and self.row_valid(index, value)
			and self.col_valid(index, value)
			and self.block_valid(index, value)
		)

	def guess_value(self, index: int, start_val) -> int:
		"""
		Given a starting point, go ahead and iterate up until 9 to see if we catch the 

		Args:
			index (int): _description_
			start_val (_type_): _description_

		Returns:
			int: _description_
		"""
		# print(f"Guessing index {index}. ", end="")
		for i in range(start_val, 10):
			# print(f"{i}...", end="")
			if (self.value_is_valid(index, i)):
				return i

	def print_puzzle(self) -> None:
		"""
		Print out the puzzle in an appealing way
		"""
		# Iterate through 0-80
		for i in range(81):
			# Subsequent print() calls use end="" so this is our way of knowing to add a new line
			if (i > 0 and (i % 9 == 0)):
				print()

			# Print a line of hyphens to show all blocks
			if (i > 0 and (i % 27 == 0)):
				print("-" * 21)

			# Print the | to show the blocks
			if (self.get_col_num(i) > 0 and (i % 3 == 0)):
				print("| ", end="")

			print(f"{self._puzzle[i]} ".replace("0", "-"), end="")

		# End on a new line
		print()

	def print_stats(self) -> None:
		"""
		Print out the statistics object - not very pretty
		"""
		if (self._keep_stats):
			print(self._statistics)
			
	def get_stats(self) -> dict:
		"""
		Get the statistics object when done

		Returns:
			dict: {
				totaltimems: [int], total milliseconds spent iterating
				totalguesses: [int], amount of times it had to guess a value for a slot
				spacestofill: [int], before solving, the amount of empy spaces to fil
				totalregressions: [int], amount of times solver had to decrement its index and try a different value
				totalretries: [int], amount of times the puzzle had to be started from the beginning
			}
		"""
		if (self._keep_stats):
			return self._statistics.copy()
		else:
			return None
		
	def bruteforce_solve(self) -> bool:
		"""
		Solve the puzzle

		Returns:
			bool: true if solved, false if unsolvable
		"""
		# Copy the original and store it. When regressing, we need to know there there was originally a value in that index
		self._original = self._puzzle.copy()

		# Iterate until we are solved
		index 	= 0
		solved	= False
		regress = False

		regressions = 0
		guesses		= 0
		retries		= 0
		blanks		= self._original.count(0)
		first_index	= 0

		starttime = time.perf_counter()
		while (not solved):
			# Determine the original value and the current one
			og 		= self._original[index]
			value 	= self._puzzle[index]
			
			# Determine if we need to make a guess or just proceed with the original value
			if (og > 0):
				# Proceed with the original value
				value = og
			elif (value == 0):
				if (first_index == None):
					first_index = index

				# No value previously, so we start our guessing from 0
				value = self.guess_value(index, 1)

				# No active safedhouse
				if (value == None):
					# print("NEED TO REGRESS")
					# self._puzzle[index] = 0
					regress = True

			else:
				self._puzzle[index] = 0
				value = self.guess_value(index, value + 1)
				if (value == None):
					# print("KEEP REGRESSING")
					regress = True
				else:
					regress = False

			if (regress):
				index		-= 1
				regressions += 1

				if (index < first_index):
					print("UNSOLVABLE")
					return False
				elif (index == first_index):
					retries += 1

			else:
				# print(f"value = {value}")
				self._puzzle[index] = value
				guesses += 1
				index	+= 1

				if (index > 80):
					solved = True

		elapsedtime = time.perf_counter() - starttime

		self._statistics['totaltimems']			= elapsedtime
		self._statistics['totalguesses'] 		= guesses
		self._statistics['spacestofill']		= blanks
		self._statistics['totalregressions'] 	= regressions
		self._statistics['totalretries']		= retries

		return True

