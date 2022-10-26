# https://leetcode.com/problems/continuous-subarray-sum/
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        # keep track of previous prefix sum
        prev_prefix = nums[0]
        
        # keep an ongoing set of remainders seen
        remainders = set([0])
        
        for i in range(1, n):            
            # calculate current prefix.sum
            prefix = nums[i] + prev_prefix
            
            # check if current remainder was previously seen
            # the core logic is:
            #
            # if nums[i:j] % k == 0
            # then nums[:i] % k == nums[:j] % k
            if prefix % k in remainders:
                return True
            
            # record previous remainder
            remainders.add(prev_prefix % k)
            
            # update our previous prefix to current
            prev_prefix = prefix
        
        return False
