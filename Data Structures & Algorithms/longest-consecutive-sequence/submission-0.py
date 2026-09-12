class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counts = dict()

        for num in nums:
            counts[num] = True

        length = 0

        for key in counts.keys():
            curr_len = 0
            
            curr=key
            while curr in counts:
                curr_len+=1
                curr+=1

            length = max(curr_len, length)

        return length