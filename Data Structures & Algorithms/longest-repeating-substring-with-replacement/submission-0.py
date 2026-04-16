from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep a data structure containing the number of each character
        # record the maximum substring length
        # if the number of occurrences of all non-most common char is > k, l+=1
        # sliding window 
        l, r = 0, 0
        num_occurrences = defaultdict(int)
        max_length = 1
        while r < len(s):
            curr = s[r]
            num_occurrences[curr] += 1
            most_common_char = max(num_occurrences, key=num_occurrences.get)
            other_chars_num = self.getOccurrences(num_occurrences, most_common_char)
            while other_chars_num > k:
                num_occurrences[s[l]] -= 1
                l+=1
                most_common_char = max(num_occurrences, key=num_occurrences.get)
                other_chars_num = self.getOccurrences(num_occurrences, most_common_char)
            max_length = max(max_length, (r-l) + 1)
            r+=1
        return max_length


    def getOccurrences(self, char_map: dict, exclude: str) -> int:
        res = 0
        for key in char_map:
            if key != exclude:
                res += char_map[key]

        return res