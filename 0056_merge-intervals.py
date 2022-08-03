class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Python sorts by the first element of nested list
        intervals.sort()
        
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            prev = res[-1]
            
            if interval[0] <= prev[1]:
                # overlapping intervals
                prev[1] = max(prev[1], interval[1])
            else:
                # non overlapping intervals
                res.append(interval)
                
        return res
