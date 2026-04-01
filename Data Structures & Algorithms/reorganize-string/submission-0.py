from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:

        freq = Counter(s)
        heap = []
        wait = []
        res = ""


        for letter, count in freq.items():
            heapq.heappush(heap, (-count, letter))

        while heap:
            print(heap)
            count, letter = heapq.heappop(heap)
            res += letter
            
            if wait:
                heapq.heappush(heap, wait.pop())

            if abs(count) > 1:
                wait.append((count + 1, letter))
                if not heap:
                    return ""

        if wait:
            count, letter = wait.pop()
            if abs(count) > 1:
                return ""
            res += letter


        return res
        