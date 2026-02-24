from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        curr_sum, pre, res = 0, defaultdict(int), 0
        pre[0] = 1

        for n in nums:
            curr_sum += n
            target = curr_sum - k
            if target in pre:
                res += pre[target]
            pre[curr_sum] += 1

        return res
