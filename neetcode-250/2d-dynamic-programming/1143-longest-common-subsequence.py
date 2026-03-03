class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]

        for i in range(len(text1)):
            for j in range(len(text2)):
                dp[j + 1][i + 1] = (
                    dp[j][i] + 1
                    if text1[i] == text2[j]
                    else max(
                        dp[j][i + 1],  # skip character from text2
                        dp[j + 1][i],  # skip character from text1
                    )
                )

        return dp[-1][-1]
