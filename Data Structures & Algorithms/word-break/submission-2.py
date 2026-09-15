class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.dp_helper(s, wordDict, 0)
        

    def dp_helper(self, s: str, wordDict: List[str], start_idx: int) -> bool:
        if start_idx == len(s):
            return True

        possible = False
        for word in wordDict:
            if len(word) <= len(s) and s[start_idx:start_idx+len(word)] == word:
                possible = possible or self.dp_helper(s, wordDict, start_idx+len(word))

        return possible