from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_set = defaultdict(int)
        for char in s1:
            char_set[char] += 1
        
        char_counts = defaultdict(int) # holds all of the character count information for s2

        l, r = 0, 0
        while r < len(s2):
            curr = s2[r]
            char_counts[curr] += 1
            if char_counts[curr] > char_set[curr] > 0:
                while char_counts[curr] > char_set[curr]:
                    char_counts[s2[l]] -= 1
                    l += 1
            elif char_counts[curr] > char_set[curr] == 0: 
                while l <= r:
                    char_counts[s2[l]] -= 1
                    l+=1
            elif char_counts == char_set:
                return True
            
            r += 1
            
        return False