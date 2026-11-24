board = [
    [5, 0, 8, 0, 0, 0, 0, 6, 0],
    [0, 4, 2, 0, 0, 8, 0, 0, 3],
    [6, 0, 3, 0, 4, 9, 0, 0, 7],
    [8, 0, 9, 0, 3, 0, 0, 0, 0],
    [3, 7, 0, 2, 0, 1, 0, 4, 8],
    [0, 0, 0, 0, 8, 0, 3, 0, 2],
    [2, 0, 0, 1, 5, 0, 4, 0, 9],
    [1, 0, 0, 4, 0, 0, 2, 5, 0],
    [0, 5, 0, 0, 0, 0, 7, 0, 1],
]

def print_board(grid: list[list[int]]) -> None:
    for r_idx, row in enumerate(grid):
        if r_idx % 3 == 0 and r_idx != 0:
            print("-" * 21)
        line = []
        for c_idx, val in enumerate(row):
            if c_idx % 3 == 0 and c_idx != 0:
                line.append("|")
            line.append(str(val) if val != 0 else "-")
        print(" ".join(line))

# MAIN
print_board(board)