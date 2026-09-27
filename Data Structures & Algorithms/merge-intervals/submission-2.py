class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        out = [intervals[0]]
        for start, end in intervals:
            if out[-1][1] >= start:
                out[-1][1] = max(out[-1][1], end)
            else:
                out.append([start, end])

        return out 