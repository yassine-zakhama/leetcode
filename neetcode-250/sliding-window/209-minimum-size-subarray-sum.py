from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res, curr_sum, left = 100001, 0, 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            if curr_sum >= target:
                while curr_sum - nums[left] >= target:
                    curr_sum -= nums[left]
                    left += 1
                res = min(res, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return res if res != 100001 else 0
