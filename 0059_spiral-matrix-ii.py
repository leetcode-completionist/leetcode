class Solution:
    """
    This problem is very similar to spiral-matrix.
    
    Instead of reading from a matrix, we write to a matrix.
    """
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        
        res = [[None] * n for i in range(n)]
        
        expected_size = n * n
        
        num = 1
        while num < expected_size + 1:
            # left to right
            for i in range(left, right + 1):
                res[top][i] = num
                num += 1
            
            # top to bottom
            for i in range(top + 1, bottom + 1):
                res[i][right] = num
                num += 1
            
            # if we moved to a new row
            if bottom > top:
                # right to left
                for i in range(right - 1, left - 1, -1):
                    res[bottom][i] = num
                    num += 1
            
            # if we moved to a new col
            if right > left:
                # bottom to top
                for i in range(bottom - 1, top, -1):
                    res[i][left] = num
                    num += 1
            
            # shrink boundaries
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        
        return res
