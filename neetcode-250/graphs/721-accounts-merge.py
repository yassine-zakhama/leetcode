from collections import defaultdict
from typing import List


# O(E * log(E))
class Solution:
    def find(self, x):
        root = x

        while self.parent[root] != root:
            root = self.parent[root]

        while x != root:
            parent = self.parent[x]
            self.parent[x] = root
            x = parent

        return root

    def unify(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_owner, self.parent, self.rank = {}, {}, {}

        for owner_id in range(len(accounts)):
            self.parent[owner_id] = owner_id
            self.rank[owner_id] = 1

            for j in range(1, len(accounts[owner_id])):
                email = accounts[owner_id][j]
                if email in email_owner:
                    self.unify(owner_id, email_owner[email])
                else:
                    email_owner[email] = owner_id

        flat_emails = defaultdict(list)
        for email, owner_id in email_owner.items():
            root_owner = self.find(owner_id)
            flat_emails[root_owner].append(email)

        res = []
        for owner_id, emails in flat_emails.items():
            emails.sort()
            res.append([accounts[owner_id][0]] + emails)
        return res
