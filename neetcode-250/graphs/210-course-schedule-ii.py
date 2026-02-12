from collections import defaultdict
from typing import List


# O(V + E) time and space
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = defaultdict(list)
        for course, prerequisite in prerequisites:
            pre[course].append(prerequisite)

        res, visited, visiting = [], set(), set()

        def top_sort(node):
            if node in visited:
                return False
            if node in visiting:
                return True

            visiting.add(node)

            for nei in pre[node]:
                if top_sort(nei):
                    return True

            visiting.remove(node)
            visited.add(node)

            res.append(node)
            return False

        for course in range(numCourses):
            if top_sort(course):
                return []

        return res
