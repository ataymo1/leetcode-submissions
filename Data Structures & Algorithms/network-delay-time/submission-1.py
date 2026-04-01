from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        adj = defaultdict(list)

        for src, target, weight in times:
            adj[src].append((target, weight))
        
        heap = [(0, k)]
        shortest = {}

        while heap:
            weight, src = heapq.heappop(heap)
            if src in shortest:
                continue
            
            print(f"{src} : {weight}")
            shortest[src] = weight
            
            for next_node, cost in adj[src]:
                if next_node not in shortest:
                    heapq.heappush(heap, (cost + weight, next_node))
        
        if len(shortest) != n:
            return -1
        
        return max(shortest.values())
            







        