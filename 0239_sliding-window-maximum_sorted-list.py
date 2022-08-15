# https://leetcode.com/problems/sliding-window-maximum/
from sortedcontainers import SortedList

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        
        sorted_list = SortedList()
        
        for i in range(len(nums)):
            sorted_list.add(nums[i])
            
            if len(sorted_list) > k:
                # evict older nums from list
                sorted_list.remove(nums[i - k])
            
            if len(sorted_list) == k:
                res.append(sorted_list[-1])
        
        return res
