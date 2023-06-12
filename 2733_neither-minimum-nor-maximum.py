class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        max_n = max(nums)
        min_n = min(nums)
        
        for num in nums:
            if num != max_n and num != min_n:
                return num
        
        return -1
