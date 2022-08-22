# https://leetcode.com/problems/wiggle-sort/
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        wiggle_up = True
        
        prev = 0
        for i in range(1, len(nums)):
            if wiggle_up:
                if nums[prev] > nums[i]:
                    # wiggle up is violated, we swap
                    nums[prev], nums[i] = nums[i], nums[prev]
                
            else:
                # wiggle down
                if nums[prev] < nums[i]:
                    # wiggle down is violated, we swap
                    nums[prev], nums[i] = nums[i], nums[prev]
            
            prev = i
            wiggle_up = not wiggle_up
