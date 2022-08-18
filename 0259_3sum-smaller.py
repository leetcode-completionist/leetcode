# https://leetcode.com/problems/3sum-smaller/
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        if n < 3:
            # can't get three sum with less than three numbers
            return 0
        
        # it is okay to sort because we only care about
        # how MANY triplets and not specifically the indices of
        # these triplets
        nums.sort()
        
        res = 0
        
        for i in range(n - 2):
            # for each number, we attempt to find how many two sums
            # in the following elements.
            #
            # we stop right at the 3rd to last element, because we
            # need at least two more elements to find a three sum.
            res += self.twoSumSmaller(nums, i + 1, target - nums[i])
        
        return res
            
            
    def twoSumSmaller(self, nums: List[int], start: int, target: int) -> int:
        res = 0
        
        l, r = start, len(nums) - 1
        
        while l < r:
            if nums[l] + nums[r] >= target:
                # too large, look at the next smaller number
                r -= 1
                continue
            
            # if nums[l] + nums[r] < target
            # then that means all numbers between l+1 and r-1
            # can also be used to form a twosum with nums[l]
            #
            # this gives us (r - l) pairs
            res += r - l
            
            # move the l pointer up and try again
            l += 1
        
        return res
