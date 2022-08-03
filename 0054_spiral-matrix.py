class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        
        res = []
        expected_size = len(matrix) * len(matrix[0])
        
        while len(res) < expected_size:
            # left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            
            # top to bottom
            for i in range(top + 1, bottom + 1):
                res.append(matrix[i][right])
            
            # if we moved to a new row
            if bottom > top:
                # right to left
                for i in range(right - 1, left - 1, -1):
                    res.append(matrix[bottom][i])
            
            # if we moved to a new col
            if right > left:
                # bottom to top
                for i in range(bottom - 1, top, -1):
                    res.append(matrix[i][left])
            
            # shrink boundaries
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        
        return res
