from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        curr_product = 1
        for i in range(len(nums)):
            res[i], curr_product = curr_product, curr_product * nums[i]
        curr_product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i], curr_product = res[i] * curr_product, curr_product * nums[i]
        return res
