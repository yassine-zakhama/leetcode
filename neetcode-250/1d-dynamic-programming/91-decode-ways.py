class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        prev2, prev1 = 1, 1

        for i in range(1, len(s)):
            curr = 0

            if s[i] != "0":
                curr += prev1

            if "10" <= s[i - 1 : i + 1] <= "26":
                curr += prev2

            prev2, prev1 = prev1, curr

        return prev1


# O(n) time and space
class Solution2:
    def numDecodings(self, s: str) -> int:
        cache = {len(s): 1}

        def decode(i):
            if i in cache:
                return cache[i]

            take_one = decode(i + 1) if s[i] != "0" else 0
            take_two = (
                decode(i + 2) if i < len(s) - 1 and "10" <= s[i : i + 2] <= "26" else 0
            )

            cache[i] = take_one + take_two
            return cache[i]

        return decode(0)
