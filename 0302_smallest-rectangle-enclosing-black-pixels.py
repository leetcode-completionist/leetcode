# https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/
class Solution:
    def minArea(self, image: List[List[str]], row: int, col: int) -> int:
        m, n = len(image), len(image[0])
        
        # use binary search to find the first row with a "1"
        top, bottom = 0, row
        while top < bottom:
            mid = top + (bottom - top) // 2
            if any(cell == "1" for cell in image[mid]):
                bottom = mid
            else:
                top = mid + 1
        upper_bound = top
        
        # use binary search to find the last row with a "1"
        top, bottom = row, m - 1
        while top < bottom:
            mid = bottom - (bottom - top) // 2
            if any(cell == "1" for cell in image[mid]):
                top = mid
            else:
                bottom = mid - 1
        lower_bound = top
        
        # use binary search to find the first col with a "1"
        left, right = 0, col
        while left < right:
            mid = left + (right - left) // 2
            if any(image[i][mid] == "1" for i in range(m)):
                right = mid
            else:
                left = mid + 1
        left_bound = left
        
        # use binary search to find the last col with a "1"
        left, right = col, n - 1
        while left < right:
            mid = right - (right - left) // 2
            if any(image[i][mid] == "1" for i in range(m)):
                left = mid
            else:
                right = mid - 1
        right_bound = left
        
        # find the total area
        return (lower_bound - upper_bound + 1) * (right_bound - left_bound + 1)
