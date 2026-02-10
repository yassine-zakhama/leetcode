from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        def reverse(prev, node):
            next = node.next
            node.next = prev
            return reverse(node, next) if next else node

        return reverse(None, head)


class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        next = head.next
        head.next = None

        while next:
            temp = next.next
            next.next = head
            head = next
            next = temp

        return head
