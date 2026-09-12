class Solution:
    def countSubstrings(self, s: str) -> int:
        # backtracking solution seems best here
        # maybe we can track each substring purely by its start/end indices and then vary those

        num_palindromes = 0

        for start in range(len(s)):
            for end in range(start, len(s)):
                l, r = start, end

                # a b c d

                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1

                num_palindromes += (l >= r)
                #print(s[start:end])

        return num_palindromes