# https://leetcode.com/problems/set-mismatch/
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = 0
        
        repeated = 0
        for num in nums:
            bit = 1 << num
            if seen & bit == 0:
                seen |= bit
            else:
                # already seen
                repeated = num  
            
        for i in range(1, len(nums) + 1):
            if seen & (1 << i) == 0:
                # not seen
                return [repeated, i]
            
        raise Exception("invalid test case")
