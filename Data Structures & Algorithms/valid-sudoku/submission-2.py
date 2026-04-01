class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        for i in range(9):
            store = [0] * 9
            for j in range(9):
                value = board[i][j]
                if value != ".":
                    value = int(value)
                    print(value)
                    if store[value-1] == 0:
                        store[value-1] = 1
                    else:
                        return False
        
        for i in range(9):
            store = [0] * 9
            for j in range(9):
                value = board[j][i]
                if value != ".":
                    value = int(value)
                    if store[value-1] == 0:
                        store[value-1] = 1
                    else:
                        return False
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                store = [0] * 9
                for k in range(3):
                    for l in range(3):
                        value = board[i + k][j + l]
                        if value != ".":
                            value = int(value)
                            if store[value-1] == 0:
                                store[value-1] = 1
                            else:
                                return False

        return True




        




