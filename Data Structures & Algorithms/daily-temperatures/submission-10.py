class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # dynamic programming
        n = len(temperatures)
        result = [0 for _ in range(n)]

        for i in range(n - 2, -1, -1):
            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
        
        return result