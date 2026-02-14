from typing import List


# O(n) space and time
class Solution:
    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:
            x, self.parent[x] = self.parent[x], root
        return root

    def unify(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return True

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.rank[root_x] += self.rank[root_y]
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += self.rank[root_x]

        return False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parent = [i for i in range(len(edges) + 1)]
        self.rank = [1 for i in range(len(edges) + 1)]

        res = None
        for u, v in edges:
            if self.unify(u, v):
                res = [u, v]
        return res
