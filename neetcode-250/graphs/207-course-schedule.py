from collections import defaultdict
from typing import List


# O(V + E) = O(numCourses + prerequisites)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        for course, prerequisite in prerequisites:
            pre[course].append(prerequisite)

        visited, visiting = set(), set()

        def has_cycle(node):
            if node in visiting:
                return True
            if node in visited:
                return False

            visited.add(node)

            visiting.add(node)
            for nei in pre[node]:
                if has_cycle(nei):
                    return True
            visiting.remove(node)

            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False
        return True
