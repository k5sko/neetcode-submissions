class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # dynamic programming
        n = len(temperatures)
        result = [0 for _ in range(n)]

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if result[j] == 0:
                    j = n
                    break
                j += result[j]
            
            if j < n:
                result[i] = j - i
    
        return result