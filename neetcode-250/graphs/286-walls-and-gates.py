from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:
            level = len(queue)
            while level:
                level -= 1
                r, c = queue.popleft()

                if (
                    r + 1 != ROWS
                    and grid[r + 1][c] != -1
                    and grid[r][c] + 1 < grid[r + 1][c]
                ):
                    grid[r + 1][c] = grid[r][c] + 1
                    queue.append((r + 1, c))

                if r != 0 and grid[r - 1][c] != -1 and grid[r][c] + 1 < grid[r - 1][c]:
                    grid[r - 1][c] = grid[r][c] + 1
                    queue.append((r - 1, c))

                if (
                    c + 1 != COLS
                    and grid[r][c + 1] != -1
                    and grid[r][c] + 1 < grid[r][c + 1]
                ):
                    grid[r][c + 1] = grid[r][c] + 1
                    queue.append((r, c + 1))

                if c != 0 and grid[r][c - 1] != -1 and grid[r][c] + 1 < grid[r][c - 1]:
                    grid[r][c - 1] = grid[r][c] + 1
                    queue.append((r, c - 1))
