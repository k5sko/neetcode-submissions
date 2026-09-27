class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # not sorted
        # [1 2 3 4 1]
        # implement a bucket sort
        # do an LSD radix sort
        # min_elem, max_elem = min(nums), max(nums)
        from collections import defaultdict
        frequencies = [set() for _ in range(len(nums) + 1)]
        num_freq = defaultdict(int)

        # frequences = {0: {}, 1: {1}, 3: {2}}
        # num_freq = {1: 1, 2: 2}
        for num in nums:
            freq = num_freq[num] # 3
            if freq == 0:
                frequencies[0].add(num)
            num_freq[num] += 1
            frequencies[freq].remove(num)
            frequencies[freq+1].add(num)
        
        # frequences = {0: {}, 1: {1}, 2: {2}, 3: {3}}
        # num_freq = {1: 1, 2: 2, 3: 3} 
        elems = [] 
        idx = len(nums)
        while len(elems) < k:
            elems.extend(frequencies[idx])
            idx -= 1

        return elems