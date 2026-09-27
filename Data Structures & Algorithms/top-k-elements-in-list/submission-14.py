from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # not sorted
        # [1 2 3 4 1]
        # implement a bucket sort
        # do an LSD radix sort
        # min_elem, max_elem = min(nums), max(nums)
        num_freq = Counter(nums)

        # frequences = {0: {}, 1: {1}, 3: {2}}
        # num_freq = {1: 1, 2: 2}
        
        frequencies = [set() for _ in range(max(num_freq.keys()))]
        for num, freq in num_freq.items():
            frequencies[freq-1].add(num)

        # frequences = {0: {}, 1: {1}, 2: {2}, 3: {3}}
        # num_freq = {1: 1, 2: 2, 3: 3} 
        elems = [] 
        idx = max(num_freq.keys()) - 1
        while len(elems) < k:
            elems.extend(frequencies[idx])
            idx -= 1

        return elems