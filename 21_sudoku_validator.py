"""Validate a completed 9x9 Sudoku grid."""
def valid_sudoku(grid: list[list[int]]) -> bool:
    if len(grid) != 9 or any(len(row) != 9 for row in grid):
        return False
    expected = set(range(1, 10))
    if any(set(row) != expected for row in grid):
        return False
    if any({grid[row][col] for row in range(9)} != expected for col in range(9)):
        return False
    return all(
        {grid[row][col] for row in range(box_row, box_row + 3)
         for col in range(box_col, box_col + 3)} == expected
        for box_row in (0, 3, 6) for box_col in (0, 3, 6)
    )

if __name__ == "__main__":
    solution = [[(row * 3 + row // 3 + col) % 9 + 1 for col in range(9)] for row in range(9)]
    print("Valid" if valid_sudoku(solution) else "Invalid")
