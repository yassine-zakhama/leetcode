from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, curr_total):
            if i == len(nums):
                return curr_total
            return dfs(i + 1, curr_total ^ nums[i]) + dfs(i + 1, curr_total)

        return dfs(0, 0)
