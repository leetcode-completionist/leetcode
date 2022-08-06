class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (r + l) // 2
                        
            if ((mid - 1 < l or nums[mid - 1] < nums[mid]) and
                (mid + 1 > r or nums[mid + 1] < nums[mid])):
                # mid is larger than both of its neighbors (if any)
                # it qualifies as a peak
                return mid

            # we do not care which side (left, right) we go
            # we just need to find A peak.

            elif mid > l and nums[mid - 1] > nums[mid]:
                # left is higher, we can go left
                r = mid - 1
                
            elif mid < r and nums[mid + 1] > nums[mid]:
                # right is higher, we can go left
                l = mid + 1
                
            else:
                raise Exception("illega state - binary search")
            
        raise Exception("illega state - no peak found")
