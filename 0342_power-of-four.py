# https://leetcode.com/problems/power-of-four/
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        # if n is a power of four, then it would
        # satisfy the following:
        #
        #   n = 4^x, where n is an integer
        #
        # we can rearrange the terms using the log function
        #
        #   log2(n) = x * log2(4)
        #
        # this can be simplified into
        #
        #       log2(n) = x * log2(2^2)
        #               = x * 2 * log2(2)
        #               = x * 2
        #   log2(n) / 2 = x
        #
        # now we just need to make sure x is an integer
        # another way of looking at this is that log2(n)
        # is divisible by 2
        return math.log2(n) % 2 == 0
