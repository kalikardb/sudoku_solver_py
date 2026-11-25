from sudoku_solver import sudokusolver

# Difficulty: 1/10 - Starting baseline puzzle with a moderate number of clues
# and straightforward early constraints.
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

# Difficulty: 2/10 - High clue density with lots of forced single-candidate
# cells, causing very few dead ends in a brute-force search.
sample2 = [
    5, 3, 0, 6, 7, 8, 9, 1, 2,
    6, 7, 2, 1, 9, 5, 3, 4, 8,
    1, 9, 8, 3, 4, 2, 5, 6, 7,
    8, 5, 9, 7, 6, 1, 4, 2, 3,
    4, 2, 6, 8, 5, 3, 7, 9, 1,
    7, 1, 3, 9, 2, 4, 8, 5, 6,
    9, 6, 1, 5, 3, 7, 2, 8, 4,
    2, 8, 7, 4, 1, 9, 6, 3, 5,
    3, 4, 5, 2, 8, 6, 1, 7, 0,
]

# Difficulty: 3/10 - Slightly more blanks across rows and columns, creating
# occasional early branches that resolve quickly.
sample3 = [
    5, 0, 4, 6, 0, 8, 9, 0, 2,
    6, 7, 0, 1, 9, 0, 3, 4, 0,
    0, 9, 8, 3, 4, 2, 0, 6, 7,
    8, 0, 9, 7, 0, 1, 4, 0, 3,
    4, 2, 0, 8, 5, 0, 7, 9, 0,
    0, 1, 3, 9, 2, 4, 0, 5, 6,
    9, 0, 1, 5, 0, 7, 2, 0, 4,
    2, 8, 0, 4, 1, 0, 6, 3, 0,
    0, 4, 5, 2, 8, 6, 0, 7, 9,
]

# Difficulty: 4/10 - Fewer givens in the top rows, forcing your solver to
# backtrack more often near the beginning of the array.
sample4 = [
    5, 0, 0, 6, 0, 0, 9, 0, 0,
    0, 7, 2, 0, 9, 5, 0, 4, 8,
    1, 0, 8, 3, 0, 2, 5, 0, 7,
    8, 5, 0, 7, 6, 0, 4, 2, 0,
    4, 0, 6, 8, 0, 3, 7, 0, 1,
    7, 1, 0, 9, 2, 0, 8, 5, 0,
    9, 6, 0, 5, 3, 0, 2, 8, 0,
    2, 0, 7, 4, 0, 9, 6, 0, 5,
    3, 4, 0, 2, 8, 0, 1, 7, 0,
]

# Difficulty: 5/10 - Balanced medium-level sparsity where several valid
# candidates compete in early cells before constraints narrow down.
sample5 = [
    0, 3, 4, 0, 7, 8, 0, 1, 2,
    6, 0, 0, 1, 0, 0, 3, 0, 0,
    1, 9, 0, 3, 4, 0, 5, 6, 0,
    8, 0, 9, 0, 6, 1, 0, 2, 3,
    4, 2, 0, 8, 0, 3, 7, 0, 1,
    0, 1, 3, 9, 2, 0, 8, 5, 0,
    9, 0, 1, 0, 3, 7, 0, 8, 4,
    2, 8, 0, 4, 0, 9, 6, 0, 5,
    0, 4, 5, 2, 8, 0, 1, 7, 0,
]

# Difficulty: 6/10 - Noticeably fewer clues in the upper-left and middle
# blocks, increasing search depth before dead ends are detected.
sample6 = [
    5, 0, 0, 0, 7, 0, 0, 1, 0,
    0, 7, 0, 1, 0, 5, 0, 0, 8,
    1, 0, 8, 0, 4, 0, 5, 6, 0,
    0, 5, 0, 7, 0, 1, 0, 2, 0,
    4, 0, 6, 0, 5, 0, 7, 0, 1,
    0, 1, 0, 9, 0, 4, 0, 5, 0,
    9, 0, 1, 0, 3, 0, 2, 0, 4,
    0, 8, 0, 4, 0, 9, 0, 3, 0,
    3, 0, 5, 0, 8, 0, 1, 0, 9,
]

# Difficulty: 7/10 - Sparse row starts and fewer cross-box anchors, leading
# to frequent regressions across multiple rows.
sample7 = [
    0, 0, 4, 6, 0, 0, 0, 1, 0,
    6, 0, 0, 0, 9, 0, 3, 0, 0,
    0, 9, 0, 3, 0, 2, 0, 0, 7,
    8, 0, 0, 0, 6, 0, 4, 0, 0,
    0, 2, 0, 8, 0, 3, 0, 9, 0,
    7, 0, 0, 0, 2, 0, 8, 0, 0,
    0, 6, 0, 5, 0, 7, 0, 0, 4,
    2, 0, 0, 0, 1, 0, 6, 0, 0,
    0, 4, 0, 2, 0, 6, 0, 0, 9,
]

# Difficulty: 8/10 - Low clue count with wide-open early indices; a great
# stress test for recursion/loop depth and state cleanup on backtrack.
sample8 = [
    5, 0, 0, 0, 0, 8, 0, 0, 0,
    0, 0, 2, 1, 0, 0, 0, 4, 0,
    0, 9, 0, 0, 4, 0, 5, 0, 0,
    0, 0, 9, 0, 0, 1, 0, 0, 3,
    4, 0, 0, 8, 0, 0, 7, 0, 0,
    0, 1, 0, 0, 2, 0, 0, 5, 0,
    0, 0, 1, 0, 0, 7, 0, 0, 4,
    2, 0, 0, 4, 0, 0, 0, 3, 0,
    0, 4, 0, 0, 8, 0, 0, 0, 9,
]

# Difficulty: 9/10 - Very sparse board (~24 clues) where early guesses look
# plausible for many steps before failing deep in the grid.
sample9 = [
    0, 3, 0, 0, 0, 0, 9, 0, 0,
    0, 0, 2, 0, 9, 0, 0, 4, 0,
    1, 0, 0, 3, 0, 0, 0, 0, 7,
    0, 0, 9, 0, 0, 1, 0, 0, 0,
    0, 2, 0, 8, 0, 3, 0, 9, 0,
    7, 0, 0, 0, 2, 0, 8, 0, 0,
    0, 6, 0, 5, 0, 0, 0, 0, 4,
    0, 0, 7, 0, 1, 0, 6, 0, 0,
    3, 0, 0, 0, 0, 6, 0, 7, 0,
]

# Difficulty: 10/10 - Minimalist high-backtrack test (~21 clues) with long
# stretches of zeros, pushing a basic brute-force solver hardest.
sample10 = [
    0, 0, 4, 0, 0, 0, 0, 1, 0,
    6, 0, 0, 0, 9, 0, 0, 0, 8,
    0, 9, 0, 3, 0, 0, 5, 0, 0,
    0, 0, 0, 0, 6, 0, 0, 2, 0,
    4, 0, 0, 8, 0, 3, 0, 0, 1,
    0, 1, 0, 0, 2, 0, 0, 0, 0,
    0, 0, 1, 0, 0, 7, 0, 8, 0,
    2, 0, 0, 0, 1, 0, 0, 0, 5,
    0, 4, 0, 0, 0, 0, 1, 0, 0,
]

all_tests = [sample1, sample2, sample3, sample4, sample5, sample6, sample7, sample8, sample9, sample10]
for test in all_tests:
	print("======   NEW   ======")
	solver = sudokusolver(test, False)
	solver.print_puzzle()

	solved = solver.bruteforce_solve()
	print()
	
	if (solved):
		print("======   PAU   ======")
		solver.print_puzzle()
		solver.print_stats()
	else:
		print("Unsolvable!")	
	print()
		
