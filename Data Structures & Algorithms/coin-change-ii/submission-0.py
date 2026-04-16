from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
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