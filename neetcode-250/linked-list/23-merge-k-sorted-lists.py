import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(n * log(k)) time, O(k) space
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap, counter = [], 0
        for l in lists:
            if l:
                heap.append((l.val, counter, l))
                counter += 1

        heapq.heapify(heap)
        dummy = current = ListNode()
        while heap:
            node = heapq.heappop(heap)[2]
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1
            current.next = current = node
        return dummy.next
