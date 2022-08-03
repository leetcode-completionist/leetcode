class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        
        res = []
        for i in range(len(nums)):
            num = nums[i]
            if i > 0 and num == nums[i - 1]:
                # we already tried this combination
                continue
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                left = nums[l]
                right = nums[r]
                total = num + left + right
                
                if total > 0:
                    # too big, decrease right pointer
                    r -= 1
                elif total < 0:
                    # too small, increase left pointer
                    l += 1
                else:
                    # we have a match
                    res.append([num, left, right])
                    
                    # keep moving left pointer until we see a new number
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    
        return res
