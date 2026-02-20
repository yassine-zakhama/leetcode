from typing import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, count, left = len(s1), Counter(s1), 0

        for right, right_char in enumerate(s2):
            count[right_char] -= 1

            while count[right_char] < 0:
                count[s2[left]] += 1
                left += 1

            if right - left + 1 == s1_len:
                return True

        return False
