class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        heap = []
        res = []
        newstart, newend = newInterval

        heapq.heappush(heap, tuple((newstart, -newend)))

        for start, end in intervals:
            heapq.heappush(heap, tuple((start, -end)))
        first = heapq.heappop(heap)
        res.append([first[0], -first[1]])
        while heap:
            # print(heap)
            interval = heapq.heappop(heap)
            start, end = interval
            # print(res[-1])
            if start > res[-1][0]:
                if start > res[-1][1]:
                    res.append([start, -end])
                else:
                    if -end > res[-1][1]:
                        res[-1][1] = -end

        return res


                

            




            

        
        

        





        


            
        