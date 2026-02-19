class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        maj, count, i = nums[0], 1, 1
        while i < len(nums):
            if nums[i] == maj:
                count += 1
            elif count == 1:
                maj = nums[i]
            else:
                count -= 1
            i += 1
        return maj
