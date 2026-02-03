from typing import List


letters = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


class Solution:
    # O(n * (4^n)), where n is len(digits)
    def letterCombinations(self, digits: str) -> List[str]:
        res, curr_comb = [], []

        def generate_combs(i):
            if i == len(digits):
                res.append("".join(curr_comb))
                return

            for l in letters[digits[i]]:
                curr_comb.append(l)
                generate_combs(i + 1)
                curr_comb.pop()

        generate_combs(0)
        return res
