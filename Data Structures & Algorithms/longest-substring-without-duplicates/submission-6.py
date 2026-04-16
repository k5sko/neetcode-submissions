class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        chars = set()

        # TODO: define l and r pointers
        
        l=0
        r=0

        while r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l+=1
            
            chars.add(s[r])

            length = max(length, r-l+1)
            r+=1
        
        return length
        """
        while right pointer in scope:
            add right pointer to charset
            check if theres any duplicates by doing while loop (condition is that left pointer char is in charset)
            we need to move the right pointer + 1 (do this at end to avoid OOB errors)
        """