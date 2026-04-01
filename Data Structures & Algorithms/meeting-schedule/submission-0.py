"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        new_intervals = []
        for i in intervals:
            new_intervals.append((i.start, i.end))

        new_intervals.sort()

        cur_time = 0
        for start, end in new_intervals:
            if start < cur_time:
                return False
            cur_time = end

        return True
