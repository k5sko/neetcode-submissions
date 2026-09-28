class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()

        def dp(idx: int, remaining: int, count: int) -> int:
            if remaining == 0:
                return count
            
            if idx < 0:
                return amount + 1
            
            best = amount + 1
            for amt in range(1 + remaining//coins[idx]):
                best = min(best, dp(idx - 1, remaining - amt * coins[idx], count + amt))
            return best

        res = dp(len(coins) - 1, amount, 0)

        if res <= amount:
            return res
        else:
            return -1