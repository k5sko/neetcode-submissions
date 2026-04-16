class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Start off with a brute force solution and then see where we can go
        # What we could do is check if any word in the dictionary matches the start of the string from idx i
        # recurse over idx i until we can't proceed
        # if we stop because idx == len(s), true
        # if we stop with idx < len(s), false

        # go from end and build up to idx = 0
        wordSet = set(wordDict)
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for idx in range(1, len(s)+1):
            for word in wordSet:
                n = len(word)
                if idx >= n and s[idx-n:idx] == word:
                    dp[idx] = dp[idx-n]
                    if dp[idx]:
                        break
        return dp[len(s)]
