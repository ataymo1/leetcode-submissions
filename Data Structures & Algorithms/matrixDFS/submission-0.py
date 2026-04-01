class Solution:
    count = 0;

    def countPaths(self, grid: List[List[int]]) -> int:
        self.seek(0, 0, grid)
        return self.count
        
    
    def seek(self, i, j, grid):

        if(i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 1):
            return
        
        if(i == len(grid)-1 and j == len(grid[0])-1):
            self.count += 1
            return
        
        grid[i][j] = 1
        
        self.seek(i+1, j, grid)
        self.seek(i, j+1, grid)
        self.seek(i-1, j, grid)
        self.seek(i, j-1, grid)

        grid[i][j] = 0
        
        return

        





        
        

        