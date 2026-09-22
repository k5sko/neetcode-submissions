class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        dp = [0] * len(temperatures)

        for i in range(n, -1, -1):
            for j in range(i+1, n):
                if temperatures[i] < temperatures[j]:
                    dp[i] = j - i
                    break

        return dp