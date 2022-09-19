# https://leetcode.com/problems/sparse-matrix-multiplication/
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        res = [[0] * len(mat2[0]) for _ in range(len(mat1))]
        
        for mat1_i in range(len(mat1)):
            mat1_row = mat1[mat1_i]
            
            # mat1_row dot product every mat2_col
            for mat2_j in range(len(mat2[0])):
                
                s = 0
                for mat2_i in range(len(mat2)):
                    s += mat2[mat2_i][mat2_j] * mat1_row[mat2_i]
                
                res[mat1_i][mat2_j] = s
        
        return res
