class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums = sorted(nums)
        self.topk = nums[-k:]
        self.bottom = [-i for i in nums[:k]]

        heapq.heapify(self.bottom)
        heapq.heapify(self.topk)

    def add(self, val: int) -> int:
        if len(self.topk) == 0:
            heapq.heappush(self.topk, val)
            return val
            
        print(self.topk, self.bottom, "\n")
        if val > self.topk[0]:
            if len(self.topk) == self.k:
                itemToDrop = heapq.heappushpop(self.topk, val)
                heapq.heappush(self.bottom, -1 * itemToDrop)
                return self.topk[0]
            else:
                heapq.heappush(self.topk, val)
                return self.topk[0]
        else:
            heapq.heappush(self.bottom, -1 * val)
            return self.topk[0]

"""
self.topk = [3 3 5]
self.bottom = [-3 -1 -2]
"""