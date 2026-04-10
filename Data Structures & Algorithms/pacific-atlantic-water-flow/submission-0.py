class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        reach_pacific = set()
        reach_atlantic = set()


        p_visited = set()
        a_visited = set()

        for row in range(len(heights)):
            self.bfs(tuple((row, len(heights[0]) - 1)), reach_atlantic, heights, a_visited)
        
        for col in range(len(heights[0])):
            self.bfs(tuple((len(heights) - 1, col)), reach_atlantic, heights, a_visited)

        for row in range(len(heights)):
            self.bfs(tuple((row, 0)), reach_pacific, heights, p_visited)
        
        for col in range(len(heights[0])):
            self.bfs(tuple((0, col)), reach_atlantic, heights, p_visited)


        intersected = a_visited & p_visited
        sol = []

        for pos in intersected:
            sol.append(pos)
        return sol
        

        
    def bfs(self, pos, output, heights, visited):
        if pos in visited:
            return
        visited.add(pos)
        output.add(pos)
        
        row, col = pos
        
        water_level = heights[row][col]
        neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

        for n in neighbors:
            n_row, n_col = n
            if n_row >= len(heights) or n_col >= len(heights[0]) or n_row < 0 or n_col < 0 or heights[n_row][n_col] < water_level:
                continue
            self.bfs(tuple((n_row, n_col)), output, heights, visited)







