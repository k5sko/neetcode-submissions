class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        import math

        distances = []
        for point in points:
            x, y = point
            distances.append((math.sqrt(x ** 2 + y ** 2), point))

        heapq.heapify(distances)
        
        closest = [] # heap
        
        for _ in range(k):
            closest.append(heapq.heappop(distances)[1])

        return closest