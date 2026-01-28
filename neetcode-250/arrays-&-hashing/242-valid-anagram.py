from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_char_count = defaultdict(int)
        for c in s:
            s_char_count[c] += 1

        for c in t:
            if not s_char_count[c]:
                return False
            s_char_count[c] -= 1
        return True
