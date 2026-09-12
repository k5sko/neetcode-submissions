class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        keys = set(nums)

        length = 0
        for num in nums:
            if num-1 in keys:
                continue

            curr_length = 1
            while num+curr_length in keys:
                curr_length+=1
            
            length = max(curr_length, length)

        return length