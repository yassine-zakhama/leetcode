from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        queue, fresh = deque(), set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                elif grid[r][c] == 2:
                    queue.append((r, c))

        if not fresh:
            return 0

        minutes = 0
        while queue:
            minutes += 1

            length = len(queue)
            while length:
                length -= 1
                r, c = queue.popleft()
                for candidate in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if candidate in fresh:
                        queue.append(candidate)
                        fresh.remove(candidate)

        return minutes - 1 if not fresh else -1
