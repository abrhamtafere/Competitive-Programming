class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        no_rows, no_colms = len(matrix), len(matrix[0])
        self.sumMatrix = [[0] * (no_colms+1) for i in range(no_rows+1)]
        
        for row in range(no_rows):
            prefix_sum = 0
            for colm in range(no_colms):
                prefix_sum += matrix[row][colm]
                pre_sum_above = self.sumMatrix[row][colm+1]
                self.sumMatrix[row+1][colm+1] = prefix_sum + pre_sum_above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1

        lower_right = self.sumMatrix[row2][col2]
        upper_left = self.sumMatrix[row1-1][col1-1]
        pre_sum_above = self.sumMatrix[row1-1][col2]
        left = self.sumMatrix[row2][col1-1]

        return lower_right - pre_sum_above - left + upper_left
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
