from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()

        def visit(r, c):
            key = (r, c)
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or key in visited
                or grid[r][c] == "0"
            ):
                return 0

            visited.add(key)
            visit(r + 1, c)
            visit(r - 1, c)
            visit(r, c + 1)
            visit(r, c - 1)
            return 1

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res += visit(r, c)
        return res
