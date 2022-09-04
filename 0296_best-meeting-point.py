# https://leetcode.com/problems/best-meeting-point/
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # we take advantage of the fact that we can only
        # travel manhattan distances (e.g. up/down/left/right)
        #
        # this allows us to collapse our 2D problem into
        # two separate 1D problems.
        #
        # given an array (e.g. 1 0 1 0 0 0 1)
        # the min distance traveled will be at the median of
        # houses (i.e. i = 2)
        #
        # given an array with even houses (e.g. 1 0 1 0 1 0 1)
        # the min distance traveled will also be at the median
        # (i.e. i = 3)
        rows = []
        cols = []
        
        # collect indices of each houses into rows and cols
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
                    
        rows.sort()
        cols.sort()
        
        def minDistance(points: List[int]) -> int:
            distance = 0
            
            l, r = 0, len(points) - 1
            while l < r:
                # doesn't matter where the median is,
                # two points must travel the same
                # TOTAL distance in order to meet
                #
                # if the # of points are odd, the median
                # point is when l == r, a distance of 0
                #
                # if the # of points are even, the median
                # is between two points, a disance of r - l
                distance += points[r] - points[l]
                l += 1
                r -= 1
                
            return distance
        
        # add up min distance traveled horizontally
        # and vertically
        return minDistance(rows) + minDistance(cols)
