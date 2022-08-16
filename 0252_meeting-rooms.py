# https://leetcode.com/problems/meeting-rooms/
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
            if intervals[i][0] == intervals[i - 1][0]:
                return False
            
        return True
