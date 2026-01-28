from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, n in enumerate(nums):
            if target - n in indices:
                return [i, indices[target - n]]
            indices[n] = i
