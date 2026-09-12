class Solution:
    def countSubstrings(self, s: str) -> int:
        # backtracking solution seems best here
        # maybe we can track each substring purely by its start/end indices and then vary those

        num_palindromes = 0

        for start in range(len(s)):
            for end in range(start+1, len(s)+1):
                num_palindromes += self.check_palindrome(s[start:end])

        return num_palindromes
    
    def check_palindrome(self, s: str) -> bool:
        n = len(s)
        for idx in range(n//2):
            if s[idx] != s[n - 1 - idx]:
                return False

        return True