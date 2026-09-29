class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        dp:
        [[1, 0, 0, 0], 
         [1, 0, 0, 0],
         [1, 0, 0, 0]]
        """
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins) + 1)] # number of ways to make amt for each subset of coins 
        for i in range(len(coins)):
            dp[i][0] = 1
 
        for idx in range(1, len(coins) + 1):
            for amt in range(1, amount+1):
                coin = coins[idx-1]
                for total_coin in range(1 + amt//coin):
                    dp[idx][amt] += dp[idx-1][amt-(coin * total_coin)]
        
        return dp[-1][-1]
