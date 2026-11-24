board = [
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


def print_board(grid: list[int], step: int | None = None) -> None:
	if step is not None:
		print(f"Step {step}:")
	for r_idx in range(9):
		if r_idx % 3 == 0 and r_idx != 0:
			print("-" * 21)
		row = grid[r_idx * 9 : (r_idx + 1) * 9]
		cells = [str(v) if v != 0 else "-" for v in row]
		print(f"{' '.join(cells[0:3])} | {' '.join(cells[3:6])} | {' '.join(cells[6:9])}")

def get_row_num(index: int) -> int:
	return index // 9

def get_col_num(index: int) -> int:
	return index % 9

def get_block_num(index: int) -> int:
	row_num = get_row_num(index)
	col_num = get_col_num(index)

	return ((row_num // 3) * 3) + (col_num // 3)

def row_valid(index: int, value: int) -> bool:
	row_num = get_row_num(index)
	start 	= row_num * 9
	end 	= start + 9

	# print(f"row:{row_num} ", end="")
	for i in range(start, end):
		# print(f"r[{i}]={board[i]} ", end="")
		if (board[i] == value):
			return False
	# print()

	return True

def col_valid(index: int, value: int) -> bool:
	col_num = get_col_num(index)

	# print(f"col:{col_num} ", end="")
	for i in range(9):
		col_index = (i * 9) + col_num
		# print(f"c[{col_index}]={board[col_index]} ", end="")
		if (board[col_index] == value):
			return False
	# print()

	return True

def block_valid(index: int, value: int) -> bool:
	row_num_block	= get_row_num(index) // 3
	col_num_block	= get_col_num(index) // 3


	start = ((row_num_block * 3) * 9) + (col_num_block * 3)

	block_num = get_block_num(index)
	# print(f"blk:{block_num} (start:{start}) ", end="")

	for i in range(9):
		row		= i % 3
		col 	= i // 3

		block_index	= (start + row) + (col * 9)
		# print(f"b[{block_index}]={board[block_index]} ", end="")
		if (board[block_index] == value):
			return False
	# print()

	return True

def value_is_valid(index: int, value: int) -> bool:
    return (
		board[index] == 0
		and row_valid(index, value)
		and col_valid(index, value)
		and block_valid(index, value)
	)

# MAIN
def main():
	print_board(board)

	# i = 77
	# print(f"I:{i} V:{board[i]} R:{get_row_num(i)} C:{get_col_num(i)} B:{get_block_num(i)}")
	# print(value_is_valid(i, 4))

	### TEST ###
	for i in range(81):
		if (value_is_valid(i, 7)):
			print(f"7 is valid at index {i}")
			print(f"I:{i} V:{board[i]} R:{get_row_num(i)} C:{get_col_num(i)} B:{get_block_num(i)}")

if __name__ == "__main__":
    main()