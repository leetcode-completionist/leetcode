# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # create a list of time tuples        
        times = list(zip(plantTime, growTime))
        
        # sort by growTime in descending order
        times.sort(key = lambda x : -x[1])
        
        res = 0
        
        # keep track of latest bloom time
        cur = 0
        for plant, grow in times:
            # add plantTime
            cur += plant
            
            # take the later time between
            # res and if current flower blooms
            res = max(res, cur + grow)
            
        return res
