import math

class Solution:
    
    def getPermutation(self, n: int, k: int) -> str:
        # available digits
        digits = [str(i) for i in range(1, n + 1)]
        
        k -= 1 # zero index based
        
        res = ""
        
        for i in range(n, 0, -1):
            # for n digits, there are n buckets
            # each with a size of (n - 1)!
            bucket_size = math.factorial(i - 1)
            
            # our offset is determined by our k
            offset = k // bucket_size
            
            # bucket start is offset * bucket_size
            bucket_start = offset * bucket_size
            
            # offset also applies to our available digits arr
            digit = digits[offset]
            
            res += digit
            
            # remove digit from being used again
            digits.remove(digit)
            
            # we update k as we get closer to our sequence
            k -= bucket_start
        
        return res
