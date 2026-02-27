# O(n * m * k) time, O(n + m * k)
# n = len(s)
# m = len(wordDict)
# k = max length of a word in wordDict
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(dp)):
            if not dp[i]:
                continue
            for word in words:
                if s.startswith(word, i):
                    dp[i + len(word)] = True

        return dp[-1]
