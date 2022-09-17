# https://leetcode.com/problems/matrix-diagonal-sum/
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        
        primary_sum = 0
        secondary_sum = 0
        for idx in range(n):
            primary_sum += mat[idx][idx]
            secondary_sum += mat[n - 1 - idx][idx]
            
        center = 0
        if n % 2 != 0:
            center = mat[n // 2][n // 2]
            
        return primary_sum + secondary_sum - center
