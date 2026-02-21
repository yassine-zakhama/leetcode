class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        dp = set([0])
        for n in nums:
            if n == target:
                return True
            for n2 in list(dp):
                if n2 + n == target:
                    return True
                if n2 + n < target:
                    dp.add(n2 + n)

        return False
