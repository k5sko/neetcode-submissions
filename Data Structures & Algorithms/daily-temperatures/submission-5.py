from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # keep track of a sequence of non-increasing days and when you see a day that's larger than the last you have the closest day warmer than all of those

        # keep a stack instead

        r = 1
        n = len(temperatures)

        result = [0] * n
        current_less_than = deque()
        current_less_than.append((temperatures[0], 0))
        

        while r < n:
            while len(current_less_than) > 0 and current_less_than[-1][0] < temperatures[r]:
                temperature, day = current_less_than.pop()
                result[day] = r - day
            
            current_less_than.append((temperatures[r], r))
            
            r += 1
            
        return result