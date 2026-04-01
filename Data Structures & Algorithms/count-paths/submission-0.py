from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:


        #base cases: bounds of grid (0), at location (1)
        #add the left and the right
        @cache
        def dp(row, col, count):
            if row < 0 or row >= m or col < 0 or col >= n:
                return 0
            if row == m-1 and col == n-1:
                return 1
            
            return dp(row, col+1, count) + dp(row + 1, col, count)
        
        return dp(0, 0, 0)
        

        

            





        