from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        option1, option2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            option1, option2 = option2, min(option1, option2) + cost[i]
        return min(option1, option2)
