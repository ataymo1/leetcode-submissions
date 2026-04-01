class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        res = ""
        heap = []
        last = deque()
        waiting = []

        if a > 0:
            heapq.heappush(heap, (-a, "a"))
        if b > 0:
            heapq.heappush(heap, (-b, "b"))
        if c > 0:
            heapq.heappush(heap, (-c, "c"))

        while heap:
            count, letter = heapq.heappop(heap)

            if waiting:
                heapq.heappush(heap, waiting.pop())

            if len(last) == 2:
                if last[0] == letter and last[1] == letter:
                    waiting.append((count, letter))
                    continue
                else:
                    last.popleft()
                    last.append(letter)
            else:
                last.append(letter)
            
            res += letter
            if abs(count) > 1:
                heapq.heappush(heap, (count + 1, letter))

        return res
                


            

