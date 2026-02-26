class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(len(dp)):
            if dp[i] == 0:
                continue
            for n in nums:
                nxt = i + n
                if nxt < len(dp):
                    dp[nxt] += dp[i]

        return dp[target]
