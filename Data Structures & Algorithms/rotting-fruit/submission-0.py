class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        queue = deque()
        time = 0

        def isFreshFruit(grid):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return True
            return False

        if not isFreshFruit(grid):
            return 0

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))

        while queue:

            if not isFreshFruit(grid):
                return time
                
            for i in range(len(queue)):
                row, col = queue.popleft()

                neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for drow, dcol in neighbors:
                    nrow = row + drow
                    ncol = col + dcol

                    if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]) and grid[nrow][ncol] == 1:
                        queue.append((nrow, ncol))
                        grid[nrow][ncol] = 2
            
            time += 1
        
        if isFreshFruit(grid):
            return -1
        else:
            return time
            
        
        