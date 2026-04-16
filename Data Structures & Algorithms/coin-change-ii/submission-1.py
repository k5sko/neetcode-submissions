from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        @cache
        def dfs(idx: int, remaining_needed: int):
            total_ways = 0

            if idx >= len(coins):
                return 0
            
            if remaining_needed == 0:
                return 1
            elif remaining_needed < 0:
                return 0

            total_ways += dfs(idx+1, remaining_needed)
            total_ways += dfs(idx, remaining_needed-coins[idx])

            return total_ways

        return dfs(0, amount)
        """
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]

        for i in range(n+1):
            dp[i][0] = 1

        for idx in range(n-1, -1, -1): # index of the current coin we're considering
            for amount_left in range(1, amount+1): # how much more do we have to add
                if coins[idx] > amount_left:
                    dp[idx][amount_left] = dp[idx+1][amount_left]
                else:
                    dp[idx][amount_left] = dp[idx+1][amount_left] + dp[idx][amount_left - coins[idx]]

        return dp[0][amount]