class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        # maybe some sort of binary search
        # we could potentially binary search over the values that work
        low, high = 1, max(piles)

        while low < high:
            rate = (low + high)//2
            # hoursTaken
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/rate)

            if h < hours:
                low = rate + 1
            elif h >= hours:
                high = rate
            
        return high