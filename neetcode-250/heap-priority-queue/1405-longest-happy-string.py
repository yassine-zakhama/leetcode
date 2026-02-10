import heapq


# O((a + b + c) * log3)
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for candidate in [[-a, "a"], [-b, "b"], [-c, "c"]]:
            if candidate[0] != 0:
                heapq.heappush(heap, candidate)

        res = []
        while heap:
            count1, char1 = heapq.heappop(heap)
            if len(res) < 2 or not (res[-2] == res[-1] == char1):
                res.append(char1)
                remaining1 = -count1 - 1
                if remaining1 > 0:
                    heapq.heappush(heap, [-remaining1, char1])
                continue

            if not heap:
                break

            count2, char2 = heapq.heappop(heap)
            res.append(char2)
            remaining2 = -count2 - 1
            if remaining2 > 0:
                heapq.heappush(heap, [-remaining2, char2])
            heapq.heappush(heap, [count1, char1])

        return "".join(res)
