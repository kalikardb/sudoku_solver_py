# Sudoku Solver (Python)

A Python Sudoku solver built around a `sudokusolver` class that represents the 9×9 grid as a flat 81-element 1D list (`0` for empty cells, `1–9` for digits). It uses iterative brute-force backtracking with row, column, and 3×3 block validation, along with optional run statistics.

## How It Works

* **1D Grid Representation (`0–80`):** Stores the 9×9 board in a single 81-element list and maps indices to rows (`index // 9`), columns (`index % 9`), and 3×3 blocks (`((row // 3) * 3) + (col // 3)`).
* **Input Validation:** `sudokusolver(puzzle, keep_stats)` validates on instantiation that `puzzle` is a `list` of `81` integers in the `0–9` range.
* **Iterative Backtracking (`bruteforce_solve()`):** Tries candidate values `1–9` in blank cells, checks row/column/block validity, and regresses backward when no valid candidate remains.
* **Optional Statistics (`keep_stats=True`):** Tracks search metrics during a solve and exposes them via `print_stats()` and `get_stats()` (`totaltimems`, `totalguesses`, `spacestofill`, `totalregressions`, and `totalretries`).

## Usage

```python
from sudoku_solver import sudokusolver

puzzle = [
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

solver = sudokusolver(puzzle, keep_stats=True)
solver.print_puzzle()

if solver.bruteforce_solve():
    print("\nSolved:")
    solver.print_puzzle()
    solver.print_stats()
else:
    print("\nUnsolvable!")