class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # rename everything because it is too hard to reason otherwise
        a_left, a_right = ax1, ax2
        b_left, b_right = bx1, bx2
        
        a_bottom, a_top = ay1, ay2
        b_bottom, b_top = by1, by2
        
        # calculate individual areas first
        a_area = (a_right - a_left) * (a_top - a_bottom)
        b_area = (b_right - b_left) * (b_top - b_bottom)
        
        # determine overlapping area (if any)
        if b_right <= a_left or b_left >= a_right:
            # no overlap
            return a_area + b_area
        
        if b_top <= a_bottom or b_bottom >= a_top:
            # no overlap
            return a_area + b_area
        
        # the overlapping width is difference between middle two points
        horizontal = sorted([a_left, a_right, b_left, b_right])
        overlapping_width = horizontal[2] - horizontal[1]
        
        # the overlapping height is different between middel two points
        vertical = sorted([a_bottom, a_top, b_bottom, b_top])
        overlapping_height = vertical[2] - vertical[1]
        
        # subtract overlapping area from the total area
        return a_area + b_area - (overlapping_width * overlapping_height)
