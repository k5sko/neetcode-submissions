class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = [stone * -1 for stone in stones]
        heapq.heapify(stone_heap)

        while len(stone_heap) > 1:
            x = heapq.heappop(stone_heap) * -1
            y = heapq.heappop(stone_heap) * -1
            if x == y:
                continue
            
            heapq.heappush(stone_heap, -1*(x-y))

        return len(stone_heap) and -1 * stone_heap[0]