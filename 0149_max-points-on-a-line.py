class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # every point starts off on a line with itself
        res = [1] * len(points)
        
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            
            # count number of duplicates
            dup_count = 0
            
            # count number of points on a vertical line
            vertical_count = 0
            
            # count number of points on a horizontal line
            horizontal_count = 0
            
            # count number of points on the same sloped line
            max_slope_count = 0

            slope_to_points = defaultdict(lambda: 0)
            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                if x2 == x1 and y2 == y1:
                    # same coordinates
                    dup_count += 1

                elif x2 == x1:
                    # on a vertical line
                    vertical_count += 1
                    
                elif y2 == y1:
                    # on a horizontal line
                    horizontal_count += 1
                    
                else:
                    if x2 < x1:
                        # make sure x2,y2 is to the right of x1,y1
                        # so that all our slopes are consistent
                        delta_x = x1 - x2
                        delta_y = y1 - y2
                    else:
                        delta_x = x2 - x1
                        delta_y = y2 - y1

                    # GUH this is the trick to this question
                    #
                    # Because floating point division is inaccurrate,
                    # we have to reduce our slope to coprimes.
                    # 
                    # By finding the GCD and dividing it from both deltas,
                    # it reduces the same slope (e.g. 1/2, 2/4, 4/8) down to
                    # the same coprimes (i.e. 1/2)
                    gcd = math.gcd(delta_x, delta_y)
                    
                    # We are okay with dividing our slope by GCD because it
                    # will remain an integer without losing precision
                    slope = (delta_x // gcd, delta_y // gcd)
                    
                    # increase the point count for this slope
                    slope_to_points[slope] += 1
                
            if slope_to_points:
                # it is possible for us to find no matching points on
                # any sloped lines
                max_slope_count = max(slope_to_points.values())
            
            # store the largest number of points on any line + any duplicates
            res[i] += dup_count + max(vertical_count,
                                      horizontal_count,
                                      max_slope_count)
        
        return max(res)
