class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        # now insert into max-heap
        max_heap = []
        for key in freq:
            heapq.heappush(max_heap, (freq[key], key))

        while len(max_heap) > k:
            heapq.heappop(max_heap)

        return [key for freq, key in max_heap]

"""
1 -> 3
2 -> 2
3 -> 1

max_heap = []
for key = 1:
    heap => [(-3, 1)]

    key = 2:
    heap => [(-3, 1), (-2, 2)]

    key = 3:
    heap => [(-3, 1), (-2, 2), (-1, 3)]

"""