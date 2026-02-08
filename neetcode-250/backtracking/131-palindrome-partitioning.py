from typing import List


# O(n * 2^n)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        res, curr = [], []

        def backtrack(i):
            if i == len(s):
                res.append(curr.copy())
                return

            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    curr.append(s[i : j + 1])
                    backtrack(j + 1)
                    curr.pop()

        backtrack(0)
        return res
