# https://leetcode.com/problems/reshape-the-matrix/
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        if m * n != r * c:
            # illegal shape
            return mat
        
        res = [[0] * c for _ in range(r)]
        
        i2, j2 = 0, 0
        
        for i in range(m):
            for j in range(n):
                # iterate through every element in src matrix
                res[i2][j2] = mat[i][j]
                
                # advance pointers on the resulting matrix
                j2 += 1
                if j2 == c:
                    i2 += 1
                    j2 = 0
        
        return res
