from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if left == right:
            return head

        right_next = None

        def reverse(prev, node, curr_pos):
            nonlocal right_next
            temp = node.next
            node.next = prev
            if curr_pos == right:
                right_next = temp
                return node
            return reverse(node, temp, curr_pos + 1)

        left_prev, curr_pos = ListNode(float("inf"), head), 1
        while curr_pos != left:
            curr_pos += 1
            left_prev = left_prev.next
        left_node = left_prev.next

        left_prev.next = reverse(None, left_node, curr_pos)
        left_node.next = right_next
        return left_prev.next if left_prev.val == float("inf") else head
