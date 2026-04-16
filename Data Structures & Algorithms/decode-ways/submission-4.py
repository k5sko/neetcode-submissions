from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        """
        memo = dict()
        memo[len(s)] = 1

        def dfs(i: int):
            if i in memo:
                return memo[i]

            if i > len(s):
                return 0
            elif s[i] == "0":
                return 0

            if s[i] == "2" and i+1 < len(s) and ord(s[i+1]) > ord('6'): # if next two chars form 27, 28, or 29
                res = dfs(i+1)
                memo[i] = res
                return res
                
            elif ord(s[i]) > ord('2'):
                res = dfs(i+1)
                memo[i] = res
                return res
                            
            memo[i] = dfs(i+1) + dfs(i+2)
            return memo[i]

        return dfs(0)
        """
        # now lets do a bottom up approach
        post = 0
        curr = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "2" and i+1 < len(s) and ord(s[i+1]) > ord('6') or ord(s[i]) > ord('2'):
                curr, post = curr, curr
            elif s[i] == "0":
                curr, post = 0, curr
            else:
                curr, post = curr + post, curr

        return curr