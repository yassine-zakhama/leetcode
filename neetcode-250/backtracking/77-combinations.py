from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, curr_comb = [], []

        def do_get_comb(i):
            if i > n:
                if len(curr_comb) == k:
                    res.append(curr_comb.copy())
                return

            curr_comb.append(i)
            do_get_comb(i + 1)
            curr_comb.pop()
            do_get_comb(i + 1)

        do_get_comb(1)
        return res
