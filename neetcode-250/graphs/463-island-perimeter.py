from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        vis = set()

        def dfs(r, c):
            key = (r, c)
            if key in vis:
                return 0
            elif r < 0 or c < 0 or r == ROWS or c == COLS or not grid[r][c]:
                return 1

            vis.add(key)
            return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    return dfs(r, c)
