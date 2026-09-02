class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_prev_1, cost_prev_2 = 0, 0

        for floor in range(2, len(cost)+1):
            # cost_curr = min(cost_prev_1 + cost[floor-1], cost_prev_2 + cost[floor-2])
            cost_prev_1, cost_prev_2 = min(cost_prev_1 + cost[floor-1], cost_prev_2 + cost[floor-2]), cost_prev_1

        return cost_prev_1