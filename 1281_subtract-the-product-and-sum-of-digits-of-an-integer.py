# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        
        while n:
            digit = n % 10
            
            p *= digit
            s += digit
            
            n -= digit
            n //= 10
        
        return p - s
