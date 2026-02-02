from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, curr_perm = [], []
        picked = [False] * len(nums)

        def do_find_perm():
            if len(curr_perm) == len(nums):
                res.append(curr_perm.copy())
                return

            for i, n in enumerate(nums):
                if not picked[i]:
                    curr_perm.append(n)
                    picked[i] = True

                    do_find_perm()

                    picked[i] = False
                    curr_perm.pop()

        do_find_perm()
        return res
