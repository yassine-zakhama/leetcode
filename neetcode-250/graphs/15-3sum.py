from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def two_sum(start, target):
            seen = set()
            i = start
            while i < len(nums):
                n = nums[i]
                if target - n in seen:
                    res.append([n, -target, target - n])
                    while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                        i += 1
                seen.add(n)
                i += 1

        i = 0
        while i < len(nums) - 2:
            two_sum(i + 1, -nums[i])
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res
