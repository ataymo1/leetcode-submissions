class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if not grid:
            return -1

        if grid[0][0] == 1:
            return -1
        visited = set()
        queue = deque()
        queue.append((0, 0))
        visited.add((0, 0))
        length = 1

        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()

                if row == len(grid) - 1 and col == len(grid[0]) - 1:
                    return length

                neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]

                for drow, dcol in neighbors:
                    nrow = row + drow
                    ncol = col + dcol
                    if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]) and grid[nrow][ncol] == 0 and tuple((nrow, ncol)) not in visited:
                        visited.add((nrow, ncol))
                        queue.append((nrow, ncol))

            length += 1
        
        return -1

        



        