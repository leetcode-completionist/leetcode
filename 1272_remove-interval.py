# https://leetcode.com/problems/remove-interval/
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        for interval in intervals:
            # completely to the left, ignore
            if interval[1] <= toBeRemoved[0]:
                res.append(interval)
            
            # completely to the right, ignore
            elif interval[0] >= toBeRemoved[1]:
                res.append(interval)
            
            # interval completely within toBeRemoved
            elif interval[0] >= toBeRemoved[0] and interval[1] <= toBeRemoved[1]:
                # skip interval
                continue
            
            # toBeRemoved completely within interval
            elif interval[0] <= toBeRemoved[0] and interval[1] >= toBeRemoved[1]:
                if interval[0] != toBeRemoved[0]:
                    res.append([interval[0], toBeRemoved[0]])
                if interval[1] != toBeRemoved[1]:
                    res.append([toBeRemoved[1], interval[1]])
            
            # partially covered left, move left until no longer covered
            elif interval[0] >= toBeRemoved[0]:
                interval[0] = toBeRemoved[1]
                res.append(interval)
                
            # partially covered right, move right until no longer covered
            elif interval[1] <= toBeRemoved[1]:
                interval[1] = toBeRemoved[0]
                res.append(interval)
            
        return res
