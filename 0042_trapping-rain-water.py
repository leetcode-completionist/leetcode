class Solution:
    def trap(self, height: List[int]) -> int:
        h_len = len(height)
        left_largest = [None] * h_len
        right_largest = [None] * h_len
        
        # Keep an array of largest seen from left-to-right
        for i in range(h_len):
            if i == 0:
                left_largest[i] = height[i]
            else:
                left_largest[i] = max(left_largest[i - 1], height[i])
                
        # Keep an array of largest seen from right-to-left
        for i in range(h_len - 1, -1, -1):
            if i == h_len - 1:
                right_largest[i] = height[i]
            else:
                right_largest[i] = max(right_largest[i + 1], height[i])
        
        res = 0
        for i in range(h_len):
            # Look to the left for largest value possible (l)
            # Look to the right for largest value possible (r)
            # max(min(l, r) - height[i], 0) will be amount of water at index i
            res += max(min(left_largest[i], right_largest[i]) - height[i], 0)
        
        return res
