class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode(0, 0, None, self.head)
        self.head.next = self.tail

    def move_to_front(self, key: int):
        node = self.cache[key]

        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.move_to_front(key)
        return self.cache[key].val

    def evict_end(self):
        node = self.tail.prev

        node.prev.next = self.tail
        self.tail.prev = node.prev
        del self.cache[node.key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.move_to_front(key)
            self.cache[key].val = value
            return

        if len(self.cache) == self.capacity:
            self.evict_end()

        node = ListNode(key, value, self.head.next, self.head)
        self.head.next.prev = node
        self.head.next = node
        self.cache[key] = node
