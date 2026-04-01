class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.product = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

        for i in range(len(self.product)):
            for j in range(len(self.product[0])):
                total = matrix[i][j]
                if i > 0:
                    total += self.product[i-1][j]
                if j > 0:
                    total += self.product[i][j-1]
                if i > 0 and j > 0:
                    total -= self.product[i-1][j-1]
                self.product[i][j] = total
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        changes = 0
        cur_sum = self.product[row2][col2]
        if col1 > 0:
            cur_sum -= self.product[row2][col1-1]
            changes += 1
        if row1 > 0:
            cur_sum -= self.product[row1-1][col2]
            changes += 1
        if changes == 2:
            cur_sum += self.product[row1-1][col1-1]
        return cur_sum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)