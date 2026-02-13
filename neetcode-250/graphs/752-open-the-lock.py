from collections import deque
from typing import List


class Solution:
    numbers = "901234567890"

    def openLock(self, deadends: List[str], target: str) -> int:
        start, self.visited = "0000", set(deadends)

        if start in self.visited:
            return -1
        self.visited.add(start)

        queue, turns = deque([start]), 0
        while queue:
            for _ in range(len(queue)):
                candidate = queue.popleft()
                if candidate == target:
                    return turns
                self.add_next(candidate, queue)
            turns += 1

        return -1

    def add_next(self, s, queue):
        for i, c in enumerate(s):
            digit = int(c)

            next1 = s[:i] + self.numbers[digit] + s[i + 1 :]
            if next1 not in self.visited:
                self.visited.add(next1)
                queue.append(next1)

            next2 = s[:i] + self.numbers[digit + 2] + s[i + 1 :]
            if next2 not in self.visited:
                self.visited.add(next2)
                queue.append(next2)
