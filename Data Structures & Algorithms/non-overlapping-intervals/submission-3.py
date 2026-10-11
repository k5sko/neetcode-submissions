class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort based on start of each interval
        intervals.sort(key=lambda x:x[0])

        # intervals = [[1, 2], [1, 4], [2, 4]]

        # now you have a linear progression you can go through

        intervals_removed = 0
        
        l, r = 0, 0 # 0, 2
        while r < len(intervals):
            curr_endpoint = intervals[l][1] # 2
            while r < len(intervals) and intervals[r][0] < curr_endpoint:
                curr_endpoint = min(curr_endpoint, intervals[r][1])
                r += 1
            intervals_removed += (r - l) - 1
            
            l = r

        return intervals_removed