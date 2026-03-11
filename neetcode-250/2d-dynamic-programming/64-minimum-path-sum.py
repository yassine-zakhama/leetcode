class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 and c == 0:
                    continue
                if r == 0:
                    grid[r][c] += grid[r][c - 1]
                elif c == 0:
                    grid[r][c] += grid[r - 1][c]
                else:
                    grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])
        return grid[ROWS - 1][COLS - 1]
