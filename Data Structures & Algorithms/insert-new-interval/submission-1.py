class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        1. Do a binary search to find the insertion index.
        2. Insert the element at that index.
        3. Merge overlapping intervals.
            a. Merge the previous interval if it ends after the new one starts.
            b. Merge the following interval if it starts before the new one ends.
        Return the list.
        """
        if len(intervals) == 0:
            return [newInterval]
        
        new_start = newInterval[0]

        # binary search
        def bin_search():
            l, r = 0, len(intervals)-1

            while l <= r:
                m = (l+r)//2
                if intervals[m][0] == new_start:
                    return m
                elif intervals[m][0] > new_start:
                    r = m-1
                elif intervals[m][0] < new_start: # could just use else but using this for quick readability
                    l = m+1

            # to reach here, l == r must have been violated
            # just consider l
            # so start at l is too small? then we should insert to its right, so we are inserting at l+1
            # if start at l is too big? we should insert to its left, so we insert at l-1 (or r-1)
            return l
            """
            [[1, 2], [3, 5], [8, 10]]
            """

        curr = bin_search()
        intervals.insert(curr, newInterval)

        if curr > 0:
            prev = curr - 1
            if intervals[prev][1] >= intervals[curr][0]:
                temp = [intervals[prev][0], max(intervals[curr][1], intervals[prev][1])]
                intervals.pop(curr)
                intervals.pop(prev)
                intervals.insert(prev, temp)
                curr = prev

        while curr < len(intervals)-1:
            post = curr + 1
            if intervals[curr][1] >= intervals[post][0]:
                temp = [intervals[curr][0], max(intervals[post][1], intervals[curr][1])]
                intervals.pop(post)
                intervals.pop(curr)
                intervals.insert(curr, temp)
            else:
                break

        return intervals

"""
[[1,2],[3,8],[8,10],[12,16]]
curr = 1
post = 2
temp = [3, 8]
"""