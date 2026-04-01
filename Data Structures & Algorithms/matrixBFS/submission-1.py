class Solution:
    
    def shortestPath(self, grid: List[List[int]]) -> int:
        length = 0;
        queue = []
        queue.append([0, 0, length])

        while queue:
            i, j, length = queue.pop(0)
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return length
            grid[i][j] = 1;
            ns = self.neighbors(i, j, grid)
            for neighbor in ns:
                neighbor.append(length+1)
                queue.append(neighbor)
        return -1

    
    def neighbors(self, i, j, grid):
        res = []
        if i + 1 < len(grid) and grid[i+1][j] == 0:
            res.append([i+1, j])
        if i > 0 and grid[i-1][j] == 0:
            res.append([i-1, j])
        if j + 1 < len(grid[0]) and grid[i][j+1] == 0:
            res.append([i, j+1])
        if j > 0 and grid[i][j-1] == 0:
            res.append([i, j-1])
        return res