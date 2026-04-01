class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:


        visited = {}

        heap = [(0, (0, 0))]

        while heap:
            effort, pos = heapq.heappop(heap)
            row, col = pos

            if tuple((row, col)) in visited:
                continue
            
            if row == len(heights) - 1 and col == len(heights[0]) - 1:
                return effort

            visited[pos] = effort

            height = heights[row][col]

            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

            for neighbor in neighbors:
                row1, col1 = neighbor
                if row1 >= len(heights) or row1 < 0 or col1 >= len(heights[0]) or col1 < 0:
                    continue
                if neighbor not in visited:
                    heapq.heappush(heap, (max(abs(height - heights[row1][col1]), effort), (row1, col1)))


        return visited()