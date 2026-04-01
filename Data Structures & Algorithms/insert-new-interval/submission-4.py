class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        newStart, newEnd = newInterval
        for i, interval in enumerate(intervals):
            start, end = interval

            if newEnd < start:
                intervals.insert(i, newInterval)
                return intervals
            
            if newStart > end:
                continue
            
            intervals[i][0] = min(newStart, start)
            intervals[i][1] = max(newEnd, end)
            saved = i

            i += 1

            while i < len(intervals) and intervals[i][0] <= intervals[saved][1]:
                intervals[saved][1] = max(intervals[saved][1], intervals[i][1])
                del intervals[i]
            return intervals


        intervals.append(newInterval)
        return intervals

        




                

            




            

        
        

        





        


            
        