import heapq
from typing import List


# O(n * log(n))
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = [(t[0], task_idx, t[1]) for task_idx, t in enumerate(tasks)]
        sorted_tasks.sort(reverse=True)

        t, res, heap = sorted_tasks[-1][0], [], []
        while sorted_tasks or heap:
            while sorted_tasks and sorted_tasks[-1][0] <= t:
                _, task_idx, processing_t = sorted_tasks.pop()
                heapq.heappush(heap, (processing_t, task_idx))

            if heap:
                processing_t, task_idx = heapq.heappop(heap)
                res.append(task_idx)
                t += processing_t
            elif sorted_tasks:
                t = sorted_tasks[-1][0]

        return res
