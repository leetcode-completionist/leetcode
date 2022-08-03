class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])        
        res = 0
        for i in range(m):
            prev_row = matrix[i - 1] if i > 0 else [0] * n
            for j in range(n):
                if matrix[i][j] == "1":
                    matrix[i][j] = 1 + prev_row[j]
                else:
                    matrix[i][j] = 0
            res = max(res, self.largestRectangleArea(matrix[i]))
        return res

    def largestRectangleArea(self, heights: List[int]) -> int:
        # create a monotonically increasing stack
        stack = []
        
        # add a zero height at the end to flush out results for
        # previous indices
        heights.append(0)
        
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                res = max(res, (i - left - 1) * h)
            stack.append(i)            
        return res
