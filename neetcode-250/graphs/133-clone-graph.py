from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    created = {}

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        if node in self.created:
            return self.created[node]

        new_node = Node(node.val)
        self.created[node] = new_node

        for nei in node.neighbors:
            new_neighbor = self.cloneGraph(nei)
            if new_neighbor != new_node:
                new_node.neighbors.append(new_neighbor)

        return new_node
