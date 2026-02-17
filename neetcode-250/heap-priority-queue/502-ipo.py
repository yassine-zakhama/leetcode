import heapq


# O(n * log(n))
class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: list[int], capital: list[int]
    ) -> int:
        projects = [(capital[i], profits[i]) for i in range(len(profits))]
        projects.sort(key=lambda x: x[0])
        heap, i = [], 0
        while i < len(projects) and projects[i][0] <= w:
            heap.append(-projects[i][1])
            i += 1
        heapq.heapify(heap)

        while heap and k:
            k -= 1
            w += -heapq.heappop(heap)
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1

        return w
