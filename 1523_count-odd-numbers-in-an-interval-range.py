# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # get the total range of numbers
        r = high - low + 1
        
        # even amount of numbers, half of #'s will be odd
        if r % 2 == 0:
            return r // 2
        
        # odd amount of numbers, we can either have (r // 2)
        # or (r // 2) + 1 # of odds.
        #
        # for example: 3, 4, 5, 6, 7 (3 odds)
        #          or: 4, 5, 6, 7, 8 (2 odds)
        #
        # to decide which condition is true, we look at one of
        # either low/high (it doesn't matter) and see if it is
        # even or odd.
        
        # if first number is even, then there are more even
        # numbers than odd
        if low % 2 == 0:
            return r // 2
        
        # first number is odd, there are more odd numbers than even
        return (r // 2) + 1
