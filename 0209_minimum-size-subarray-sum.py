class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums:
            return 1
        
        res = math.inf
        
        l, r, curr_sum = 0, 0, nums[0]
        
        while r < len(nums):
            if curr_sum >= target:
                # the question asks for
                # "sum is greater than or equal to target"
                # current subarray fits that
                # requirement
                res = min(res, r - l + 1)
                
                # shrink the window from the left
                curr_sum -= nums[l]
                l += 1
                
                # we want to also move r if
                # l moves past r
                #
                # This is because a single number
                # could be larger than the target
                if l > r:
                    r = l
                    curr_sum = nums[l]
            else:
                # we don't have sufficient sum yet
                # so we expand our window to the right
                r += 1
                
                if r < len(nums):
                    curr_sum += nums[r]
        
        # if res remains inf, then we weren't
        # able to meet the target sum
        return res if res != math.inf else 0
