from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []

        def find_subsets(i):
            if i == len(nums):
                res.append(list(curr))
                return

            curr.append(nums[i])
            find_subsets(i + 1)
            curr.pop()
            find_subsets(i + 1)

        find_subsets(0)
        return res
