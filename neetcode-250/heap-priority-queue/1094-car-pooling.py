import heapq


class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        trips.sort(key=lambda trip: trip[1])

        heap, passengers, curr_trip = [], 0, 0
        while curr_trip < len(trips):
            curr_trip_start = trips[curr_trip][1]

            while heap and heap[0][0] <= curr_trip_start:
                passengers -= heapq.heappop(heap)[1]

            while curr_trip < len(trips) and trips[curr_trip][1] == curr_trip_start:
                passengers += trips[curr_trip][0]
                if passengers > capacity:
                    return False
                heapq.heappush(heap, (trips[curr_trip][2], trips[curr_trip][0]))
                curr_trip += 1

        return True
