from typing import List


# O(n) space and time
class Solution:
    def find(self, x):
        root = self.parent[x]
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:
            x, self.parent[x] = self.parent[x], root
        return root

    def unify(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return True

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parent = {i: i for i in range(1, len(edges) + 1)}
        self.rank = {i: 0 for i in range(1, len(edges) + 1)}

        res = None
        for u, v in edges:
            if u not in self.parent:
                self.parent[u] = u
            if v not in self.parent:
                self.parent[v] = v
            if self.unify(u, v):
                res = [u, v]
        return res
