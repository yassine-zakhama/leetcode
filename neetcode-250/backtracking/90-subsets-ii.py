from typing import List


class Solution:
    # O(n.2^n)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, curr_subset = [], []

        def do_get_subsets(i):
            if i == len(nums):
                res.append(list(curr_subset))
                return

            curr_subset.append(nums[i])
            do_get_subsets(i + 1)
            curr_subset.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            do_get_subsets(i + 1)

        nums.sort()
        do_get_subsets(0)
        return res
