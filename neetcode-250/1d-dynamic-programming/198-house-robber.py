from typing import List


# O(n) / O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i):
            if i >= len(nums):
                return 0
            if i not in cache:
                cache[i] = nums[i] + max(dfs(i + 2), dfs(i + 3))
            return cache[i]

        return max(dfs(0), dfs(1))


class Solution2:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
