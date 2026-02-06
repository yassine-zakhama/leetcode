from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev_cost, curr_cost = cost[0], cost[1]
        for i in range(2, len(cost)):
            prev_cost, curr_cost = curr_cost, min(prev_cost, curr_cost) + cost[i]
        return min(prev_cost, curr_cost)
