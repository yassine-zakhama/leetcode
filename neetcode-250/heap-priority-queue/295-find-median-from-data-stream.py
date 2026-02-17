import heapq


class MedianFinder:

    def __init__(self):
        self.min_heap, self.max_heap = [], []

    # O(log(n))
    def addNum(self, num: int) -> None:
        if self.diff() == 0:
            heapq.heappush(self.max_heap, -num)
            if not self.min_heap:
                return
        else:
            heapq.heappush(self.min_heap, num)

        if self.min_heap[0] < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    # O(1)
    def findMedian(self) -> float:
        if self.diff() == 0:
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return -self.max_heap[0]

    def diff(self):
        return abs(len(self.min_heap) - len(self.max_heap))
