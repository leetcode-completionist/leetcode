# https://leetcode.com/problems/power-of-two/
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            # 0 cannot be a power of two
            return False
        
        # the "trick" is to use bitwise operation
        # to detect if a number is a power of two
        #
        # when a number is a power of two, it will
        # ONLY have a single 1 bit followed by zero
        # or more 0 bits.
        #
        # if we subtract 1 from a power of two, it will
        # flip the rightmost 1-bit to a zero, then change
        # the remaining bits to "1".
        #
        # if we bitwise x & (x - 1), for a power of 2
        # this will result in a zero. But for any other
        # numbers, it will not be zero.
        return n & (n - 1) == 0
