from collections import defaultdict
from typing import List


# O(n * n!) time and space
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1

        res, curr = [], []

        def backtrack():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for n in counts:
                if counts[n] > 0:
                    counts[n] -= 1
                    curr.append(n)
                    backtrack()
                    curr.pop()
                    counts[n] += 1

        backtrack()
        return res
