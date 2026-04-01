class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        t = 0


        # at each step, the cost will be the max of the current t or height

        visited = {}
        heap = [(grid[0][0], 0, 0)]

        while heap:
            
            cost, row, col = heapq.heappop(heap)
            if tuple((row,col)) in visited:
                continue
            
            visited[(row,col)] = cost

            if row + 1 < len(grid) and tuple((row + 1, col)) not in visited:
                heapq.heappush(heap, (max(cost, grid[row + 1][col]), row + 1, col))

            if row - 1 >= 0 and tuple((row - 1, col)) not in visited:
                heapq.heappush(heap, (max(cost, grid[row - 1][col]), row - 1, col))

            if col + 1 < len(grid[0]) and tuple((row, col + 1)) not in visited:
                heapq.heappush(heap, (max(cost, grid[row][col + 1]), row, col + 1))

            if col - 1 >= 0 and tuple((row, col - 1)) not in visited:
                heapq.heappush(heap, (max(cost, grid[row][col - 1]), row, col - 1))

        return visited[(len(grid)-1, len(grid[0])-1)]




        