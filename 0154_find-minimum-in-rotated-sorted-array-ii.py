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
            elif nums[mid] < nums[r]:
                # otherwise, we have shifted the minimum
                # to the left half
                r = mid
            else:
                # shrink window by 1 from each side
                # because we already know nums[l] is >= nums[r]
                # at this point, and nums[mid] == nums[r]
                #
                # We are not sure where the minimum is yet.
                # But we know it will be inside nums[l + 1 : r].
                # So we retry with a slightly smaller window.
                l += 1
                r -= 1
        
        # return the larger of the two elements
        return min(nums[l], nums[r])
