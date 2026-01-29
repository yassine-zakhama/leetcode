from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen, left = set([nums[0]]), 0

        for right in range(1, len(nums)):
            left_n, right_n = nums[left], nums[right]

            if right - left > k:
                seen.remove(left_n)
            left += 1

            if right_n in seen:
                return True

            seen.add(right_n)

        return False
