# https://leetcode.com/problems/maximum-performance-of-a-team/
import heapq

class Solution:
    
    MOD = 10 ** 9 + 7
    
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # create a list of engineers (i.e. speed/efficiency tuples)
        engineers = zip(speed, efficiency)
        
        # sort by efficiency in decreasing order.
        # this makes it so that for every engineer we come across,
        # we know we have the min efficiency so far
        engineers = sorted(engineers, key = lambda x: -x[1])
        
        res = 0
        
        # we keep a min_heap of max size of k
        speed_heap = []
        
        # we keep a running total speed so we can quickly calculate
        # the current performance
        total_speed = 0
        
        for curr_speed, curr_efficiency in engineers:
            total_speed += curr_speed
            heapq.heappush(speed_heap, curr_speed)

            if len(speed_heap) > k:
                # we have more than k engineers, pop the lowest speed
                total_speed -= heapq.heappop(speed_heap)
            
            res = max(res, total_speed * curr_efficiency)
            
        return res % Solution.MOD
