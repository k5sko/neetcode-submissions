class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # you're guaranteed that start <= end
        # if you check only the ends, you don't really care what the minimum start is
        # you basically just need to check what is the earliest that we can end each interval 

        # you're comparing current end to next start, so if next start >= current end, they don't overlap. if next start < current end, they overlap. no need to sort by start since you don't need to guarantee that that's in order

        # sort based on start of each interval
        intervals.sort() # O (n log n); O(n) space (O(1) auxiliary)

        # intervals = [[1, 2], [1, 4], [2, 4]]

        # now you have a linear progression you can go through

        intervals_removed = 0
        
        l, r = 0, 0 # 0, 2
        while r < len(intervals): # Goes through array once; O(n) runtime
            curr_endpoint = intervals[l][1] # 2
            while r < len(intervals) and intervals[r][0] < curr_endpoint:
                r += 1
            intervals_removed += (r - l) - 1
            
            l = r

        return intervals_removed