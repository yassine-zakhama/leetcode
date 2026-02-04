from typing import List


class Solution:
    # O(n * k^n)
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        TOTAL = sum(nums)
        if TOTAL % k != 0:
            return False

        nums.sort(reverse=True)

        EXPECTED_SUM = TOTAL // k
        if nums[0] > EXPECTED_SUM:
            return False

        sums = [0] * k

        def backtrack(i):
            if i == len(nums):
                return True

            num = nums[i]
            for group in range(k):
                if sums[group] + num <= EXPECTED_SUM:
                    if group > 0 and sums[group - 1] == sums[group]:
                        continue

                    sums[group] += num
                    if backtrack(i + 1):
                        return True
                    sums[group] -= num

            return False

        return backtrack(0)
