from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums, res = set(nums), 0
        for n in nums:
            if (n - 1) not in nums:
                curr_len = 1
                while (n + curr_len) in nums:
                    curr_len += 1
                res = max(curr_len, res)
        return res
