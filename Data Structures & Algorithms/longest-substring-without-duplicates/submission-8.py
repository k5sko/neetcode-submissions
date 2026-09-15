class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        n = len(s)
        max_len = 0
        current_chars = set()

        # sliding window stuff
        while r < n:
            if s[r] in current_chars:
                max_len = max(max_len, r - l)
                l = r
                current_chars = {s[r]}
            else:
                current_chars.add(s[r])

            r += 1

        return max(max_len, r-l)

