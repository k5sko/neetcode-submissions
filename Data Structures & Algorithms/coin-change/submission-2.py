class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 for _ in range(amount + 1)] # min number of coins it takes to build up to this amount
        dp[0] = 0
        coin_set = set(coins)
        for amt in range(len(dp)):
            for prev_amt in range(amt):
                if amt - prev_amt in coin_set:
                    dp[amt] = min(dp[amt], dp[prev_amt] + 1) 
        
        return dp[-1] if dp[-1] <= amount else -1