from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # O(1) space
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid: slow is mid
        mid, fast = head, head
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next

        # reverse second half
        temp = mid.next
        mid.next = None
        while temp:
            temp_next = temp.next
            temp.next = mid
            mid = temp
            temp = temp_next

        # re-order
        left, right = head, mid
        while right.next:
            temp = left.next
            left.next = right
            left = temp

            temp = right.next
            right.next = left
            right = temp

        return head

    # O(n) space
    def reorderList2(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        i, j = 0, len(nodes) - 1
        while i < j:
            left, right = nodes[i], nodes[j]
            left.next = right
            right.next = nodes[i + 1]
            i += 1
            j -= 1

        nodes[i].next = None
        return nodes[0]
