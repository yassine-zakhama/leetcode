from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def do_get_total_sum(i, curr_total):
            if i == len(nums):
                return curr_total
            return do_get_total_sum(i + 1, curr_total ^ nums[i]) + do_get_total_sum(
                i + 1, curr_total
            )

        return do_get_total_sum(0, 0)
