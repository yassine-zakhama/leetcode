from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution1:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        new_nodes, temp = {}, head
        while temp:
            new_nodes[temp] = Node(temp.val)
            temp = temp.next

        temp = head
        while temp:
            new_nodes[temp].random = new_nodes.get(temp.random)
            new_nodes[temp].next = new_nodes.get(temp.next)
            temp = temp.next

        return new_nodes[head]


class Solution2:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        new_nodes = {None: None}

        def copy(node: Optional[Node]) -> Optional[Node]:
            if node in new_nodes:
                return new_nodes[node]

            new_node = Node(node.val)
            new_nodes[node] = new_node

            new_node.next = copy(node.next)
            new_node.random = copy(node.random)
            return new_node

        return copy(head)
