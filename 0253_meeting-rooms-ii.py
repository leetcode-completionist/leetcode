# https://leetcode.com/problems/meeting-rooms-ii/

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        res = 0
        min_heap = []

        for i, (start, end) in enumerate(intervals):
            while min_heap and min_heap[0][0] <= start:
                heapq.heappop(min_heap)
                
            heapq.heappush(min_heap, (end, start, i))
            
            res = max(res, len(min_heap))
            
        return res
