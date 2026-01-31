class Solution:
    def validPalindrome(self, s: str) -> bool:
        def do_check(left, right, joker):
            while left < right:
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                    continue
                return joker and (
                    do_check(left + 1, right, False) or do_check(left, right - 1, False)
                )
            return True

        return do_check(0, len(s) - 1, True)
