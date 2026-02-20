from typing import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count, res, min_count = Counter(nums), [], len(nums) // 3
        for n in count:
            if count[n] > min_count:
                res.append(n)
        return res
