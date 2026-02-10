from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        def add(l1, l2, prev_carry):
            s = l1.val + l2.val + prev_carry
            carry = 1 if s > 9 else 0
            node = ListNode(s if not carry else s % 10)

            if not l1.next and not l2.next:
                if carry:
                    node.next = ListNode(1)
                return node

            node.next = add(l1.next or ListNode(), l2.next or ListNode(), carry)
            return node

        return add(l1, l2, 0)
