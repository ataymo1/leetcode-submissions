class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        # one heap, one queue

        #     -heap will be for available tasks (min heap) [stores (time to complete, index)]
        #     -queue will be for unavailable tasks [stores (enqueue time, time to complete, index)]
        #     -solution array
        #     -cur time

        available = []
        waiting = []
        res = []
        cur_time = 0

        for index, task in enumerate(tasks):
            etime, ptime = task
            if etime == 0:
                heapq.heappush(available, (ptime, index))
            else:
                heapq.heappush(waiting, (etime, ptime, index))
        
        #     while queue and heap
        #         while queue and the head of the queue enqueue time is less than or equal to cur time
        #             popleft and push to heap
        #         if heap
        #             add to solution array
        #         else:
        #             change time to head of queue enqueue time
        #         increment time
        while available or waiting:
            while waiting and waiting[0][0] <= cur_time:
                etime, ptime, index = heapq.heappop(waiting)
                heapq.heappush(available, (ptime, index))
            if available:
                ptime, index = heapq.heappop(available)
                res.append(index)
                cur_time += ptime
            else:
                cur_time = waiting[0][0]

        
        return res
                

        
        




