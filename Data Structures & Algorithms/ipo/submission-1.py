class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        # given a list of projects

        # you can only choose k amt

        # -profits[i] tells you the profit of that project
        # -capital[i] tells you the amt of capital needed to start it

        # w is your starting capital

        # sol
        
        # two heaps:

        # - one is for jobs you can do (max heap of profits since we know we will always be able to afford them)
        # - one is for you cant do (min heap of cost and profits, when we pop we only put the profit in min heap)

        # -continue until k is done 

        available = []
        expensive = []

        for p, c in zip(profits, capital):
            if c > w:
                heapq.heappush(expensive, (c, p))
            else:
                heapq.heappush(available, -p) # max heap since we want the jobs with the most profit

        for i in range(k):
            if not available:
                break
            w += -heapq.heappop(available)

            while expensive and w >= expensive[0][0]:
                now_available = heapq.heappop(expensive)
                heapq.heappush(available, -now_available[1])
        
        return w


