class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.backtrack(tuple((i, j)), set(), word, board):
                        return True

        return False
        
        
    def backtrack(self, position, visited, left, board):

        # print(f"{position} : {visited} : {left}")
        if not left:
            return True

        row, col = position
        if position in visited or row >= len(board) or row < 0 or col >= len(board[0]) or col < 0 or board[row][col] != left[0]:
            return False

        visited.add(position)

        neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

        for n in neighbors:
            if self.backtrack(n, visited, left[1:], board):
                return True

        visited.remove(position)

        return False


    





        