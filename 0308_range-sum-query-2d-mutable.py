# https://leetcode.com/problems/range-sum-query-2d-mutable/
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.sums = []
        
        for row in self.matrix:
            self.sums.append(list(accumulate(row)))
        

    def update(self, row: int, col: int, val: int) -> None:
        self.matrix[row][col] = val
        self.sums[row] = list(accumulate(self.matrix[row]))
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for row in range(row1, row2 + 1):
            if col1 > 0:
                res += self.sums[row][col2] - self.sums[row][col1 - 1]
            else:
                res += self.sums[row][col2] 
        return res
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
