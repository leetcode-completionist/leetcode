class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # keep four pointers for the boundaries
        top, bottom = 0, len(matrix) - 1
        # top/bottom is same as left/right because matrix is a square
        left, right = top, bottom
        
        while left < right:
            for i in range(right - left):
                # i is our offset from left until right - 1
                
                # store top-left as temp
                tmp = matrix[top][left + i]
                
                # move bottom-left into top-left
                matrix[top][left + i] = matrix[bottom - i][left]
                
                # move bottom-right into bottom-left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                
                # move top-right into bottom-right
                matrix[bottom][right - i] = matrix[top + i][right]
                
                # move temp into top-right
                matrix[top + i][right] = tmp
            # shrink our boundaries
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        
