class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        l = prices[0:len(prices)//2]
        r = prices[len(prices)//2:]
        x = max(r) - min(l)

        return max(0, x, self.maxProfit(l), self.maxProfit(r))