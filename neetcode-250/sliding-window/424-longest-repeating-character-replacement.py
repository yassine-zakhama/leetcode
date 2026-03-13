from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)

        res, left, max_freq = 0, 0, 0
        for right, right_char in enumerate(s):
            count[right_char] += 1
            max_freq = max(max_freq, count[right_char])

            window = right - left + 1
            while window - max_freq > k:
                count[s[left]] -= 1
                window -= 1
                left += 1
            res = max(res, window)

        return res
