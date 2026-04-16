"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
        
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # we just need to keep track of the number of meetings currently going on at any given time. i
        # what if we keep track of the currently on-going meetings? what we could do is first heapify the intervals in 
        # O(n) based on starting time, and then one-by-one pull out the intervals. We can then store the currently on-going intervals on a heap. While the next upcoming interval has start time < end time of soonest-ending interval, add it to the heap and add 1 to the number of required conference rooms
        num_conference_rooms = 0
        intervals = sorted(intervals, key=lambda x: x.start, reverse=True) # O(n log n); could technically 
        curr_conference_rooms = []

        while len(intervals) > 0:
            newest_interval = intervals.pop() # O(1)
            if len(curr_conference_rooms) == 0 or newest_interval.start < curr_conference_rooms[0]: # 0, 0 because we need to insert as end, start to sort by end
                heapq.heappush(curr_conference_rooms, newest_interval.end)
            else:
                num_conference_rooms = max(num_conference_rooms, len(curr_conference_rooms))
                while len(curr_conference_rooms) > 0 and newest_interval.start >= curr_conference_rooms[0]:
                    heapq.heappop(curr_conference_rooms)
                heapq.heappush(curr_conference_rooms, newest_interval.end)

        num_conference_rooms = max(num_conference_rooms, len(curr_conference_rooms))

        return num_conference_rooms

"""
intervals = [[13, 17], [9, 16], [6, 20]]
n = 0
curr_conference_rooms = [8]

newest = [1, 8]
"""