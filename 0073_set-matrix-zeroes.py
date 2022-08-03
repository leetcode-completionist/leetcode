class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zero_row, zero_col = False, False
        
        # 1. determine if first row & col should be zeroes
        for i in range(m):
            if matrix[i][0] == 0:
                zero_col = True
                break
        for i in range(n):
            if matrix[0][i] == 0:
                zero_row = True
                break
        
        # 2. label rows and cols as zeroes
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 3. label all affected cells zeroes
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        # 4. zero out first row and/or col
        if zero_row:
            for i in range(n):
                matrix[0][i] = 0
        if zero_col:
            for i in range(m):
                matrix[i][0] = 0
