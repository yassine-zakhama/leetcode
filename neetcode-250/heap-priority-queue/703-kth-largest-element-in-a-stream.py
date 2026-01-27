import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.k = k - len(nums)
        self.heap = nums

    def add(self, val: int) -> int:
        if self.k:
            heapq.heappush(self.heap, val)
            self.k -= 1
        elif val > self.heap[0]:
            heapq.heappush(self.heap, val)
            heapq.heappop(self.heap)

        return self.heap[0]
        