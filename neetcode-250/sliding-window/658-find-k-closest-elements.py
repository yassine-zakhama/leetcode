import bisect


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        right = bisect.bisect_left(arr, x)
        left = right - 1

        while k:
            k -= 1
            if (
                right == len(arr)
                or left >= 0
                and abs(arr[left] - x) <= abs(arr[right] - x)
            ):
                left -= 1
            else:
                right += 1

        return arr[left + 1 : right]
