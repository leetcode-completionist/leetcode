class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        To count the number of trailing zeroes,
        we simply need to count number of factors of '5'
        in n!.
        
        The intuition behind this is that a number of
        trailing zeroes has to be divisible by 10.
        
        We can count number of 10's by looking at the prime
        factors of each number. For example:

            10! = 10*9*8*7*6*5*4*3*2*1
            
            becomes
            
            10! = (2*5)*(3*3)*(2*2*2)*
                  (7)*(2*3)*(5)*(2*2)*
                  (3)*(2)*(1)
                  
        We know that a 10 can be formed from a pair of 2 and 5.
        Note that everytime we get a 5, we have at least
        one matching 2. So we just need to count the number of
        5's.
        
        The edge case to watch out for is when a number has multiple
        factors of '5'. For example, 25, 50, 75, etc.
        """
        fives = 0
        for i in range(1, n + 1):
            n = i
            while n % 5 == 0:
                fives += 1
                n /= 5
        return fives
