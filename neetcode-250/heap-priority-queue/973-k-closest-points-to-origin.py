from cmath import sqrt
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            x, y = p
            heap.append((sqrt(x * x + y * y), p))
        heapq.heapify(heap)

        res = []
        while k:
            k -= 1
            res.append(heapq.heappop(heap)[1])
        return res
