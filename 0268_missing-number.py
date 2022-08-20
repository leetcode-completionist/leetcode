# https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # given an array with n elements
        # the missing number will either be:
        # 
        # 1. a number between [0,n)
        # 2. OR n if all elements of [0, n-1] are present
        #
        # Normally, we would use another array
        # and simply populate True for numbers found
        # and iterate for the first False in the array.
        #
        #         arr = [False] * len(nums)
        #
        #         for num in nums:
        #             if num < len(nums):
        #                 arr[num] = True
        #
        #         for num, present in enumerate(arr):
        #             if not present:
        #                 return num
        #
        #         return len(nums)
        #
        # For a constant memory solution, we need to
        # use our array itself as storage.
        n = len(nums)
        
        for i in range(n):
            if nums[i] == i:
                # element is in its rightful place
                continue
                
            if nums[i] >= n:
                # a smaller element [0,n) will be missing
                # label current cell as -1 (i.e. missing)
                nums[i] = -1
                
            # extract the number out to a var
            num = nums[i]
            
            # we assume the number is not in its rightful
            # place, so we mark the current cell as missing
            #
            # if it was already in the rightful place, we
            # will simply put it back and move on.
            nums[i] = -1
            
            # while the element is in range and
            # not in its rightful place
            while 0 <= num < n and num != nums[num]:
                # store next val in a temp var
                tmp = nums[num]
                
                # set current num in its rightful place
                nums[num] = num
                
                # we try to set the next num
                num = tmp
        
        # iterate and see first negative (i.e. missing) number
        for num, val in enumerate(nums):
            if val == -1:
                return num

        # all numbers [0, n) are present, n is our first missing number
        return n
                
