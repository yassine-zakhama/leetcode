from collections import defaultdict
from typing import List


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        pre = defaultdict(list)
        for prerequisite, course in prerequisites:
            pre[course].append(prerequisite)

        aggregated_pre = defaultdict(set)

        def dfs(node):
            if node in aggregated_pre:
                return

            for nei in pre[node]:
                dfs(nei)
                aggregated_pre[node].add(nei)
                aggregated_pre[node] |= aggregated_pre[nei]

        for course in range(numCourses):
            dfs(course)

        return [
            prerequisite in aggregated_pre[course] for prerequisite, course in queries
        ]
