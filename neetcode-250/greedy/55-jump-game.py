class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_idx = 0
        for i, n in enumerate(nums):
            if i > max_idx:
                return False
            max_idx = max(max_idx, i + n)
        return True
