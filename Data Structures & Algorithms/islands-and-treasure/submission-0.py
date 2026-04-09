class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.bfs(tuple((i, j)), grid)


    def bfs(self, pos, grid):
        distance = 0
        queue = deque()
        queue.append([pos])
        visited = set()

        while queue:
            level = queue.popleft()
            next_level = []
            print(level)
            
            for pos in level:
                row, col = pos
                if distance > grid[row][col] or pos in visited:
                    continue

                visited.add(pos)
                grid[row][col] = distance

                if row + 1 < len(grid) and grid[row + 1][col] != -1 and grid[row + 1][col] > distance + 1:
                    next_level.append(tuple((row + 1, col)))
                if row - 1 >= 0 and grid[row - 1][col] != -1 and grid[row - 1][col] > distance + 1:
                    next_level.append(tuple((row - 1, col)))
                if col + 1 < len(grid[0]) and grid[row][col + 1] != -1 and grid[row][col + 1] > distance + 1:
                    next_level.append(tuple((row, col + 1)))
                if col - 1 >= 0 and grid[row][col - 1] != -1 and grid[row][col - 1] > distance + 1:
                    next_level.append(tuple((row, col - 1)))
            if next_level:
                queue.append(next_level)
            distance += 1


                





        
        