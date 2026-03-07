class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev1_1 = prev2_1 = prev1_2 = prev2_2 = 0

        for i, n in enumerate(nums):
            if i > 0:
                curr = max(prev1_1, prev2_1 + n)
                prev2_1 = prev1_1
                prev1_1 = curr

            if i == len(nums) - 1:
                break

            curr = max(prev1_2, prev2_2 + n)
            prev2_2 = prev1_2
            prev1_2 = curr

        return max(prev1_1, prev1_2)
