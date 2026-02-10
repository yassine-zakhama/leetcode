from collections import defaultdict
import heapq


# O(len(s) * log26)
class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        heap = []
        for c in counts:
            heap.append([-counts[c], c])
        heapq.heapify(heap)

        res = []
        while heap:
            count1, char1 = heapq.heappop(heap)
            if not res or res[-1] != char1:
                res.append(char1)
                remaining1 = -count1 - 1
                if remaining1:
                    heapq.heappush(heap, [-remaining1, char1])
                continue

            if not heap:
                return ""

            count2, char2 = heapq.heappop(heap)
            res.append(char2)
            remaining2 = -count2 - 1
            if remaining2:
                heapq.heappush(heap, [-remaining2, char2])
            heapq.heappush(heap, [count1, char1])

        return "".join(res)
