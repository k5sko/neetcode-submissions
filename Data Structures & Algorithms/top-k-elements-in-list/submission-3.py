class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums.sort() # sorted
        from collections import defaultdict
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        keys = list(counts.keys())
        keys.sort(key=lambda x: counts[x], reverse=True)

        return keys[:k]