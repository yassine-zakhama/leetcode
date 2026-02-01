from collections import defaultdict
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def has_cycle(node, parent):
            if node in visited:
                return True

            visited.add(node)
            for nei in adj[node]:
                if nei != parent and has_cycle(nei, node):
                    return True
            return False

        connected = True
        for node in range(n):
            if node not in visited:
                if not connected or has_cycle(node, None):
                    return False
                connected = False
        return True
