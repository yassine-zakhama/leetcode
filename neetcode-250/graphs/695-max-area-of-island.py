from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def calc_area(r, c):
            key = (r, c)
            if (
                key in visited
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or not grid[r][c]
            ):
                return 0

            visited.add(key)
            return (
                1
                + calc_area(r + 1, c)
                + calc_area(r - 1, c)
                + calc_area(r, c + 1)
                + calc_area(r, c - 1)
            )

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, calc_area(r, c))
        return res
