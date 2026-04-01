class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        start_heap = []
        end_heap = []
        pos = 0
        people = 0
        
        for count, start, end in trips:
            heapq.heappush(start_heap, (start, count))
            heapq.heappush(end_heap, (end, count))
        
        while start_heap:
            print(f"{people}")

            while end_heap and end_heap[0][0] <= pos:
                end, count = heapq.heappop(end_heap)
                people -= count

            while start_heap and start_heap[0][0] <= pos:
                start, count = heapq.heappop(start_heap)
                if count + people > capacity:
                    return False
                people += count

            
            pos += 1
        
        return True




