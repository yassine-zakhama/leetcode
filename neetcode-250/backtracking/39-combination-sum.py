from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, curr_comb = [], []

        def find_comb(i, curr_sum):
            if i == len(candidates) or curr_sum >= target:
                if curr_sum == target:
                    res.append(list(curr_comb))
                return

            curr_comb.append(candidates[i])
            find_comb(i, curr_sum + candidates[i])
            curr_comb.pop()
            find_comb(i + 1, curr_sum)

        find_comb(0, 0)
        return res
