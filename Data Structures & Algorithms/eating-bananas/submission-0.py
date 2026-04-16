class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # each element takes ceil(piles[i]/k) hours
        # we need sum over i of ceil(piles[i]/k) <= h

        #search_space = list(range(1, max(piles)+1))
    
        # lets do a binary search for the minimum k that solves this

        l, r = 1, max(piles)
        while l <= r:
            m = (l+r)//2
            time_m = self.__time_taken_rate_k__(m, piles) # O(p) time, O(1) space

            if time_m <= h:
                r = m - 1
            else:
                l = m + 1

        return l


    def __time_taken_rate_k__(self, k: int, piles: List[int]):
        hrs = 0
        for pile in piles:
            hrs += (pile + (k-1))//k # this gives the ceil function

        return hrs