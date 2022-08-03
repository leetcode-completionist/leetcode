class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.search(nums, target, True), self.search(nums, target, False)]
        
                
    def search(self, nums: List[int], target: int, search_left) -> int:
        l, r = 0, len(nums) - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                res = mid
                if search_left:
                    r = mid - 1
                else:
                    l = mid + 1
        return res
