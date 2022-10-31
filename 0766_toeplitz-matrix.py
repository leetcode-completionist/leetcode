# https://leetcode.com/problems/toeplitz-matrix/
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        # main diagonal
        num = matrix[0][0]
        i = j = 1
        while i < m and j < n:
            if matrix[i][j] != num:
                return False
            i += 1
            j += 1
        
        # top diagonal
        for diag in range(1, n):
            i, j = 0, diag
            num = matrix[i][j]
            
            i += 1
            j += 1
            while i < m and j < n:
                if matrix[i][j] != num:
                    return False
                i += 1
                j += 1
            
        # left diagonals
        for diag in range(1, m):
            i, j = diag, 0
            num = matrix[i][j]
            
            i += 1
            j += 1
            while i < m and j < n:
                if matrix[i][j] != num:
                    return False
                i += 1
                j += 1
            
        return True
