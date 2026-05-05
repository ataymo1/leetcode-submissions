"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        heap = []

        for i in intervals:
            start, end = i.start, i.end
            heapq.heappush(heap, (start, end))

        used = []
        res = 0

        while heap:
            start, end = heapq.heappop(heap)

            while used and used[0] <= start:
                heapq.heappop(used)
            
            heapq.heappush(used, end)
            res = max(res, len(used))
        
        return res








        