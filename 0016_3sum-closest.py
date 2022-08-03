class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        
        res = 0
        diff = float('inf')
        for i in range(0, len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == target:
                    # target found, return immediately
                    return target
                
                # check if we found a closer sum
                n_diff = abs(total - target)
                if n_diff < diff:
                    res = total
                    diff = n_diff
                
                if total > target:
                    # too big, move right pointer
                    r -= 1
                else:
                    # too small, move left pointer
                    l += 1

        return res
