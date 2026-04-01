class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []
        for i, interval in enumerate(intervals):
            start, end = interval
            newStart, newEnd = newInterval
            
            if newEnd < start:
                res.append(newInterval)
                return res + intervals[i:]
            elif newStart > end:
                res.append(intervals[i])
            else:
                newInterval = [min(start, newStart), max(end, newEnd)]

        res.append(newInterval)
        return res

        




                

            




            

        
        

        





        


            
        