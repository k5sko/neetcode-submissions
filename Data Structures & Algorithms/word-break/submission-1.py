class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s == "":
            return True

        possible = False
        for word in wordDict:
            if s[:len(word)] == word:
                possible = possible or self.wordBreak(s[len(word):], wordDict)

        return possible