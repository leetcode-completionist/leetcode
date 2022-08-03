# We are given an array of size N elements
# We know that the first missing positive is either:
# (bewtween 1 and N) OR (N + 1 if every element was present)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_len = len(nums)

        for i in range(nums_len):
            if nums[i] <= 0:
                # we don't care about zero or negatives
                # so we fill it with an out-of-range integer
                nums[i] = nums_len + 1
        
        for i in range(nums_len):            
            val = abs(nums[i])
            if val <= nums_len:
                # value is within range
                # make value at (i-1) negative so we know it was found
                nums[val - 1] = -abs(nums[val - 1])

        for i, n in enumerate(nums, 1):
            if n > 0:
                # element will remain positive if (i+1) was never found
                return i

        return nums_len + 1
