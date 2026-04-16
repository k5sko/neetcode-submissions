class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        freq_to_num = [[] for num in nums]

        for num in freq:
            freq_to_num[freq[num]-1].append(num)

        collection = []
        for elem in freq_to_num[::-1]:         
            for num in elem:
                collection.append(num)

        return collection[:k]
        """
        # now insert into max-heap
        max_heap = []
        for key in freq:
            heapq.heappush(max_heap, (freq[key], key))

        while len(max_heap) > k:
            heapq.heappop(max_heap)

        return [key for freq, key in max_heap]
        """