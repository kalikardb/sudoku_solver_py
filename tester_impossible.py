from sudoku_solver import sudokusolver

# Hard 1 - Famous "AI Escargot" benchmark puzzle (17 clues): very sparse
# starting state with deep backtracking chains for brute-force solvers.
hard1 = [
    1, 0, 0, 0, 0, 7, 0, 9, 0,
    0, 3, 0, 0, 2, 0, 0, 0, 8,
    0, 0, 9, 6, 0, 0, 5, 0, 0,
    0, 0, 5, 3, 0, 0, 9, 0, 0,
    0, 1, 0, 0, 8, 0, 0, 0, 2,
    6, 0, 0, 0, 0, 4, 0, 0, 0,
    3, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 4, 1, 0, 0, 0, 0, 0, 7,
    0, 0, 7, 0, 0, 0, 3, 0, 0,
]

# Hard 2 - Sparse symmetric-style puzzle (~22 clues) with few immediate
# singles, forcing extensive trial-and-error across multiple boxes.
hard2 = [
    0, 0, 0, 0, 0, 6, 0, 0, 8,
    0, 2, 0, 0, 0, 0, 4, 0, 0,
    0, 0, 1, 0, 9, 0, 0, 5, 0,
    0, 0, 0, 4, 0, 0, 0, 7, 0,
    5, 0, 0, 0, 1, 0, 0, 0, 3,
    0, 8, 0, 0, 0, 2, 0, 0, 0,
    0, 7, 0, 0, 5, 0, 2, 0, 0,
    0, 0, 6, 0, 0, 0, 0, 9, 0,
    3, 0, 0, 8, 0, 0, 0, 0, 0,
]

# Hard 3 - Low-clue high-branching puzzle (~21 clues) with long empty runs
# that test regression cleanup and loop performance.
hard3 = [
    8, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 3, 6, 0, 0, 0, 0, 0,
    0, 7, 0, 0, 9, 0, 2, 0, 0,
    0, 5, 0, 0, 0, 7, 0, 0, 0,
    0, 0, 0, 0, 4, 5, 7, 0, 0,
    0, 0, 0, 1, 0, 0, 0, 3, 0,
    0, 0, 1, 0, 0, 0, 0, 6, 8,
    0, 0, 8, 5, 0, 0, 0, 1, 0,
    0, 9, 0, 0, 0, 0, 4, 0, 0,
]

# Impossible 1 - No duplicate initial clues in any row/col/box, but the
# digit 9 is forced into conflicting/impossible positions across units.
impossible1 = [
    1, 2, 3, 4, 5, 6, 7, 8, 0,
    0, 0, 0, 0, 9, 0, 0, 0, 0,
    0, 0, 9, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 9,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
]

# Impossible 2 - Clean initial clues with no immediate duplicates, but
# tight row/box constraints collide deep in the search tree.
impossible2 = [
	1, 2, 3, 4, 5, 6, 7, 8, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 9,
    0, 0, 9, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
]

five_tests = [hard1, hard2, hard3, impossible1, impossible2]

for test in five_tests:
	print("======   NEW   ======")
	solver = sudokusolver(test, True)
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
		
