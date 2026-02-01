from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        curr_comb, res = [], []

        def do_get_comb(i, curr_sum):
            if i == len(candidates) or curr_sum >= target:
                if curr_sum == target:
                    res.append(list(curr_comb))
                return

            curr_len = len(res)
            curr_comb.append(candidates[i])
            do_get_comb(i + 1, curr_sum + candidates[i])
            curr_comb.pop()

            if curr_len < len(res):
                while i < len(candidates) - 1 and candidates[i + 1] == candidates[i]:
                    i += 1
            do_get_comb(i + 1, curr_sum)

        do_get_comb(0, 0)
        return res
