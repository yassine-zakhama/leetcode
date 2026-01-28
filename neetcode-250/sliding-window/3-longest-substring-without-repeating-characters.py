class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        res, curr_length, left = 1, 1, 0
        seen = set([s[0]])
        for right in range(1, len(s)):
            right_char = s[right]

            if right_char not in seen:
                curr_length += 1
                seen.add(right_char)
                continue

            res = max(res, curr_length)
            while right_char in seen:
                curr_length -= 1
                seen.remove(s[left])
                left += 1
            curr_length += 1
            seen.add(right_char)

        return max(res, curr_length)
