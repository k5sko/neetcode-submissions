from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:

        @cache
        def dfs(i: int):
            if i == len(s):
                return 1
            elif i > len(s):
                return 0

            if s[i] == "0":
                return 0

            if s[i] == "2" and i+1 < len(s) and ord(s[i+1]) > ord('6'): # if next two chars form 27, 28, or 29
                return dfs(i+1)
            elif ord(s[i]) > ord('2'):
                return dfs(i+1)
                            
            return dfs(i+1) + dfs(i+2)

        return dfs(0)