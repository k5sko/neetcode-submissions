class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if n == 0:
            return []

        res = [0] * n

        from collections import deque
        stack = deque()

        r = 0

        while r < n:
            if len(stack) == 0 or temperatures[r] <= stack[-1][0]:
                stack.append((temperatures[r], r))
                r += 1
            else:
                while len(stack) > 0 and stack[-1][0] < temperatures[r]:
                    _, idx = stack.pop()
                    res[idx] = r - idx

        return res