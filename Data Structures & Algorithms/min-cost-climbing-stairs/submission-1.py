class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Thinking something DP-like
        # We need to cache total costs up till a certain point, maybe working backwards from teh end
        currentFloor = len(cost) # this is the array index

        # first just try naive soln

        """
        while currentFloor > 1: # just step down one floor at a time
            totalCost += cost[currentFloor]
            currentFloor -= 1 # instead of naively stepping down one step at a time, figure out whether one or two steps is more optimal. need to track min cost among all paths to current floor
        """

        # find min cost path to floor 0 and to floor 1
        dp = [0] * (len(cost) + 1)
        
        for floor in range(2, len(cost)+1):
            dp[floor] = min(dp[floor-1] + cost[floor-1], dp[floor-2] + cost[floor-2])

        return dp[-1]