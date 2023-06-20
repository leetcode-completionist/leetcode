class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        
        res = math.inf
        
        for i in range(1, len(nums)):
            d = nums[i] - nums[i - 1]
            res = min(res, d)
        
        return res
