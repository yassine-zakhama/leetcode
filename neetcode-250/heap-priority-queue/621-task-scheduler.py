from collections import Counter, deque
import heapq
from typing import List


# O(len(tasks))
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [[count, task] for task, count in counts.items()]
        heap.sort(reverse=True)
        for i in range(len(heap)):
            heap[i][0] = i
        heapq.heapify(heap)

        time = 0
        while heap:
            start_time, task = heapq.heappop(heap)
            if start_time > time:
                time = start_time

            counts[task] -= 1
            if counts[task] > 0:
                heapq.heappush(heap, [start_time + n + 1, task])
            time += 1
        return time


class Solution2:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-count for count in Counter(tasks).values()]
        heapq.heapify(heap)
        time, queue = 0, deque()
        while heap or queue:
            if not heap:
                remaining, start_time = queue.popleft()
                if start_time > time:
                    time = start_time
                else:
                    time += 1
                heapq.heappush(heap, remaining)
                continue

            remaining = heapq.heappop(heap)
            if remaining != -1:
                queue.append([remaining + 1, time + n + 1])
            time += 1
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        return time
