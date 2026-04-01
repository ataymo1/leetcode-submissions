class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
                        
        visited = set()
        perimeter = 0
        island = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island.append((i, j))
                    visited.add((i, j))

        for pos in island:
            row, col = pos
            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

            for neighbor in neighbors:
                row, col = neighbor
                if neighbor in visited:
                    continue
                else:
                    perimeter += 1

        return perimeter



        

            





            

                


        


            