from typing import List


# O(4^n / sqrt(n)) / O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, curr = [], []

        def backtrack(opening, closing):
            if not opening and not closing:
                res.append("".join(curr))
                return

            if opening:
                curr.append("(")
                backtrack(opening - 1, closing)
                curr.pop()

            if closing > opening:
                curr.append(")")
                backtrack(opening, closing - 1)
                curr.pop()

        backtrack(n, n)
        return res
