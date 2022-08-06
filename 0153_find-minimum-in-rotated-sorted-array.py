class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        # keep shrinking our search space until we only
        # have two elements left
        while l < r - 1:
            if nums[l] < nums[r]:
                # we already have a sorted window
                # return the smallest (i.e. left)
                return nums[l]
            
            # create a middle. The middle will
            # be included in the next iteration
            # because it could be a minimum
            mid = (r + l) // 2
            if nums[mid] > nums[r]:
                # if the middle is higher than right-most
                # value, then we must've shifted the minimum
                # to the right half
                l = mid
            else:
                # otherwise, we have shifted the minimum
                # to the left half
                r = mid
        
        # return the larger of the two elements
        return min(nums[l], nums[r])
