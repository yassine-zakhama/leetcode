from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, curr_subset = set(), []

        def do_get_subsets(i):
            if i == len(nums):
                key = tuple(curr_subset)
                if key not in res:
                    res.add(key)
                return

            curr_subset.append(nums[i])
            do_get_subsets(i + 1)
            curr_subset.pop()

            do_get_subsets(i + 1)

        nums.sort()
        do_get_subsets(0)
        return [list(s) for s in res]
