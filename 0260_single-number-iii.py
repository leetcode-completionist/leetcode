# https://leetcode.com/problems/single-number-iii/
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        
        bitmask = 0
        for num in nums:
            bitmask ^= num
        
        # at this point, bitmask == (a XOR b)
        # this cannot be zero because otherwise a == b
        #
        # to differentiate a and b, we look at their bits.
        # bitmask can ONLY have a 1 if the bit at a != the
        # bit at b
        #
        # we can get any arbitrary bit, but we can simply
        # use the rightmost bit
        
        bit = bitmask & -bitmask
        
        # next we partition the nums between two groups
        # one group has bit == 0
        # another group has bit == 1
        # 
        # a will be in one group while b will be in another group
        res = [0, 0]
        
        # after XOR every number in each group, we should be left
        # with a and b
        for num in nums:
            if num & bit == 0:
                # bit is not set
                res[0] ^= num
            else:
                # bit is set
                res[1] ^= num
        
        return res
