# O(n) time and space
class Solution:
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
