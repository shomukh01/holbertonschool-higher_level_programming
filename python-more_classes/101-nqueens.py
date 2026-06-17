#!/usr/bin/python3
"""Solves the N queens problem."""

import sys


def is_safe(queens, row, col):
    """Check if a queen can be placed at row, col."""
    for queen in queens:
        q_row = queen[0]
        q_col = queen[1]

        if q_col == col:
            return False
        if abs(q_row - row) == abs(q_col - col):
            return False
    return True


def solve(n, row, queens):
    """Find all solutions using backtracking."""
    if row == n:
        print(queens)
        return

    for col in range(n):
        if is_safe(queens, row, col):
            solve(n, row + 1, queens + [[row, col]])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve(n, 0, [])
