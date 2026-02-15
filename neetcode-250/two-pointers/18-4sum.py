from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res, l = [], 0
        while l < len(nums) - 3:
            r = l + 1

            while r < len(nums) - 2:
                curr_target = target - (nums[l] + nums[r])
                i, seen = r + 1, set()

                while i < len(nums):
                    n = nums[i]
                    if curr_target - n in seen:
                        res.append([nums[l], nums[r], n, curr_target - n])
                        while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                            i += 1
                    else:
                        seen.add(n)
                    i += 1

                while r < len(nums) - 3 and nums[r] == nums[r + 1]:
                    r += 1
                r += 1

            while l < len(nums) - 4 and nums[l] == nums[l + 1]:
                l += 1
            l += 1

        return res
