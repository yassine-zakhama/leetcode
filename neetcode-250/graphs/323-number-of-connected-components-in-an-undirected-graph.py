from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def visit(node):
            if node in visited:
                return

            visited.add(node)
            for nei in adj[node]:
                visit(nei)

        res = 0
        for v in range(n):
            if v not in adj or (v in adj and v not in visited):
                visit(v)
                res += 1
        return res
