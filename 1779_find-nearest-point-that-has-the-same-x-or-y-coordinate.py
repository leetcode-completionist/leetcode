# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def distance(a: Tuple[int], b: Tuple[int]) -> int:
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        target = (x, y)
        
        res = -1
        
        dist = math.inf
        
        for i in range(len(points)):
            point = tuple(points[i])
            
            if point[0] == target[0] or point[1] == target[1]:
                d = distance(point, target)
                if d < dist:
                    dist = d
                    res = i
                    
        return res
