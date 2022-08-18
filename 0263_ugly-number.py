# https://leetcode.com/problems/ugly-number/
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        # keep dividing by 2,3,5 until
        # we can't anymore
        #
        # this is because all other non-prime
        # factors can be reduced to 2, 3, and/or 5
        while n % 2 == 0:
            n /= 2
        while n % 3 == 0:
            n /= 3
        while n % 5 == 0:
            n /= 5
            
        # then check if the number is equal to 1
        return n == 1
