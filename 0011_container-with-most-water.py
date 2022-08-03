class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        
        l = 0
        r = len(height) - 1
        while l < r:
            height_left = height[l]
            height_right = height[r]
            
            h = min(height_left, height_right)
            res = max(res, h * (r - l))
            
            if height_right < height_left:
                r -= 1
            else:
                l += 1
        
        return res
