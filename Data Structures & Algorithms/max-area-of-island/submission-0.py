class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0
        maxArea = 0

        def dfs(i, j):
            count = 1
            grid[i][j] = 0
            if i < len(grid) - 1 and grid[i + 1][j] == 1:
                count += dfs(i + 1, j)
            if i > 0 and grid[i - 1][j] == 1:
                count += dfs(i - 1, j)
            if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                count += dfs(i, j + 1)
            if j > 0 and grid[i][j - 1] == 1:
                count += dfs(i, j - 1)
            return count

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea
