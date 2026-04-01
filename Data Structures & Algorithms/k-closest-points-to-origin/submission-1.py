class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for x, y in points:
            dist = -self.distance(x, y)

            heapq.heappush(heap, (dist, x, y))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        while heap:
            popped = heapq.heappop(heap)
            res.append([popped[1], popped[2]])

        
        return res



    def distance(self, x, y):
        return math.sqrt(x**2 + y**2)
        