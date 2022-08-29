# https://leetcode.com/problems/sort-the-matrix-diagonally/
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        res = [[None] * n for _ in range(m)]
        
        def sortDiagonal(row: int, col: int) -> None:
            diagonal = []
            
            # retrieve all elements in the diagonal
            i, j = row, col
            while i < m and j < n:
                diagonal.append(mat[i][j])
                i += 1
                j += 1
                
            diagonal.sort()
            
            # write sorted elements into the result matrix
            i, j = row, col
            k = 0
            while i < m and j < n:
                res[i][j] = diagonal[k]
                i += 1
                j += 1
                k += 1
                
        # main diagonal
        sortDiagonal(0, 0)
            
        # diagonals starting at the top
        for j in range(1, n):
            sortDiagonal(0, j)
            
        # diagonals starting at the left
        for i in range(1, m):
            sortDiagonal(i, 0)
            
        return res
