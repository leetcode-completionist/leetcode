import math

class Solution:
    # Determines if an int is a palindrome without using str()
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            # single digits are always palindromes
            return True
        
        digits = int(math.log10(x)) + 1
        
        mid = int(digits / 2)
        reversed_x = 0
        for i in range(mid):
            curr = x % 10
            x = int(x / 10)
            
            reversed_x *= 10
            reversed_x += curr
        
        if digits % 2 == 1:
            # if x is odd, drop the last digit
            x = int(x / 10)

        return x == reversed_x
