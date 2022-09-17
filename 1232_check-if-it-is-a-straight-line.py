# https://leetcode.com/problems/check-if-it-is-a-straight-line/
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort()
        
        def getSlope(a: List[int], b: List[int]) -> float:
            delta_x = b[0] - a[0]
            delta_y = b[1] - a[1]
            
            if delta_x == 0:
                return float("inf")
            
            return (b[1] - a[1]) / (b[0] - a[0])
        
        slope = getSlope(coordinates[0], coordinates[1])
        
        for i in range(2, len(coordinates)):
            if getSlope(coordinates[i - 1], coordinates[i]) != slope:
                return False
            
        return True
