class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [[math.sqrt(x[0]**2 + x[1]**2), x] for x in points]
        heapq.heapify(dists)

        return [heapq.heappop(dists)[1] for i in range(k)]