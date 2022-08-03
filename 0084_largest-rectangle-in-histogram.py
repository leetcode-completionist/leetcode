class Solution:
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
