from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes, temp = [], head
        while temp:
            nodes.append(temp)
            temp = temp.next

        node_idx = len(nodes) - n
        if node_idx == 0:
            return head.next

        prev_idx, next_idx = node_idx - 1, node_idx + 1
        nodes[prev_idx].next = nodes[next_idx] if next_idx < len(nodes) else None
        return head
