from typing import List


class Solution2:
    def rob(self, nums: List[int]) -> int:
        max_before_last, max_last = 0, 0

        for num in nums:
            temp = max(num + max_before_last, max_last)
            max_before_last = max_last
            max_last = temp
        return max_last
