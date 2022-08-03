class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        def addInterval(interval: List[int]) -> None:
            nonlocal res
            if not res:
                res.append(interval)
            elif interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        
        # Keep looping until we get to the end of the list
        # AND add the new interval to results
        i = 0
        while newInterval or i < len(intervals):
            if (i == len(intervals) or
                (newInterval and newInterval[0] < intervals[i][0])):
                # if only newInterval is remaining
                # or if newInterval has a smaller start value than
                # then next interval
                newInterval = addInterval(newInterval)
            else:
                addInterval(intervals[i])
                i += 1
                
        return res
