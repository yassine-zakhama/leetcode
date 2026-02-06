# O(n) / O(n)
class Solution:
    cache = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n not in self.cache:
            self.cache[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.cache[n]


class Solution2:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev, curr = 1, 2
        for _ in range(2, n):
            prev, curr = curr, prev + curr

        return curr
