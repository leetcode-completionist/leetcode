# https://leetcode.com/problems/palindrome-permutation/
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        bitmask = 0
        for c in s:
            # shift 1 by the ascii code number
            # and flip that bit on in the bitmask
            bitmask ^= (1 << (ord(c) - ord("a")))
            
        # if we have a palindrome, then we must have
        # 0 or 1 bit set. Any more than would mean
        # the string is not a palindrome permutation
        return bitmask & (bitmask - 1) == 0
