from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        all_chars = defaultdict(int)
        for char in t:
            all_chars[char] += 1

        currently_used = defaultdict(int)
        l, r = 0, 0
        min_l, min_r = 0, len(s) + 1

        def all_chars_present():
            for char in all_chars:
                if currently_used[char] < all_chars[char]:
                    return False
            
            return True
                

        while r < len(s):
            while all_chars_present(): # before incorporating r, so r is exclusive
                if r - l < min_r - min_l:
                    min_r, min_l = r, l

                currently_used[s[l]] -= 1
                l += 1
            
           
            curr = s[r]
            currently_used[curr] += 1
            r += 1
        
        while all_chars_present(): # before incorporating r, so r is exclusive
            if r - l < min_r - min_l:
                min_r, min_l = r, l
            currently_used[s[l]] -= 1
            l += 1
        

        if all_chars_present():
            if r - l < min_r - min_l:
                return s[l:r]
            else:
                return s[min_l:min_r]
        else:
            if min_r == len(s) + 1:
                return ""

            return s[min_l:min_r]        