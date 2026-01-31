class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.head = ListNode()
        self.tail = ListNode(0, self.head, self.head)
        self.head.next = self.tail
        self.head.prev = self.tail

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = ListNode(value, self.head.next, self.head)
        self.head.next.prev = new_node
        self.head.next = new_node

        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        node_for_removal = self.tail.prev
        self.tail.prev = node_for_removal.prev
        node_for_removal.prev.next = self.tail

        self.size += -1
        return True

    def Front(self) -> int:
        return self.tail.prev.val if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.head.next.val if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
