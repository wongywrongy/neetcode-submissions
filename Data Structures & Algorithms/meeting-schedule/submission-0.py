"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort in order first so that we can traverse in for loop 
        intervals.sort(key = lambda x : x.start)

        # start at 1 minus the length so we can do i + 1
        for i in range(len(intervals) - 1):
            if intervals[i+1].start < intervals[i].end:
                return False

        return True