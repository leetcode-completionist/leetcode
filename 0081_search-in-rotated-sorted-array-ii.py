class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                # found target
                return True
            
            # we always look to the left-most value
            if nums[l] < nums[mid]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[l] > nums[mid]:
                if nums[r] >= target and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # nums[mid] == nums[l]
                # we won't know if there are smaller numbers in between
                # iterate l once more and recheck (e.g. worst case scenario O(n))
                l += 1
        
        # we couldn't find target
        return False
        
