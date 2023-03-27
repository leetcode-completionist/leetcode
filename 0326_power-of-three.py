class Solution:
    
    MAX_POW_OF_3 = 3 ** 19
    
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (Solution.MAX_POW_OF_3 % n == 0)
