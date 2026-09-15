class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        import math

        return heapq.nsmallest(k, points, key=lambda x: math.sqrt(x[0] ** 2 + x[1] ** 2))