class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        print(intervals)
        idx = 0
        while idx < len(intervals) - 1: # idx < 2
            if intervals[idx][1] >= intervals[idx+1][0]:
                intervals[idx][1] = max(intervals[idx][1], intervals[idx+1][1])
                del intervals[idx+1]
            else:
                idx += 1

        return intervals