class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        paths = defaultdict(set)
        for edge, prob in zip(edges, succProb):
            paths[edge[0]].add((prob, edge[1]))
            paths[edge[1]].add((prob, edge[0]))

        
        visited = {}
        heap = [(1, start_node)]

        while heap:
            cost, cur = heapq.heappop(heap)
            if cur == end_node:
                return -cost
            if cur in visited:
                continue

            visited[cur] = cost

            for prob, neighbor in paths[cur]:
                if neighbor not in visited:
                    heapq.heappush(heap, (-abs(prob * cost), neighbor))

        if end_node in visited:
            return visited[end_node]

        return 0

        