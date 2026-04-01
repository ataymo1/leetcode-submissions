from functools import cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if not obstacleGrid:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # base cases: out of bounds (0), obstacle (1), at the target (1)

        # steps: go down, go right
        
        @cache
        def dp(row, col):
            if row >= m or row < 0 or col >= n or col < 0:
                return 0
            if obstacleGrid[row][col] == 1:
                return 0
            if row == m-1 and col == n-1:
                return 1
            
            return dp(row + 1, col) + dp(row, col + 1)
        
        return dp(0, 0)

        
        