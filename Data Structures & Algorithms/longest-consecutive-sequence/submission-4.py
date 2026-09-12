class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        from collections import deque, defaultdict
        
        counts = defaultdict(int)

        for num in nums:
            counts[num] = False
    
        for key in counts.keys():
            if key+1 in counts:
                counts[key] = True

        lengths = defaultdict(int)
        max_length = 0

        for key in counts.keys():
            if key in lengths:
                continue

            curr = key
            stack = deque()
            while curr in counts.keys() and curr not in lengths:
                stack.append(curr)
                curr-=1

            curr+=1
            while curr in counts:
                lengths[curr] = 1 + lengths[curr-1]
                curr += 1

            max_length = max(max_length, lengths[curr-1])           
        
        return max_length