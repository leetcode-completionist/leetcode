class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        Our previous attempt to count 5's is a linear time
        algorithm. This solution will implement a more efficient
        way to count 5's, giving us a O(log5(n)) runtime complexity.
        
        To count 5's efficiently, we will attempt to figure out
        how many 5's go into n! factorization via math.
        
            5! = 5*4*3*2*1
                 ^

            10! = 10*9*8*7*6*5!
                   ^         ^

            15! = 15*14*13*12*11*10!
                   ^              ^

            20! = 20*19*18*17*16*15!
                   ^              ^
        
        Look like we just need to calculate n/5.
        But what aboout n = 25?
        
            25! = 5*5*24*23*22*21*20!
                  ^ ^              ^
              
        Now there are two additional factors of 5 instead.
        To accommodate this, we just need to calculate n/25
        as well.
        
        What happens if there are three "5"s? or
        four "5"s? Eventually we get the following:
        
            fives = n/5 + n/25 + n/125 + ...
        
        At some point, the denominator will exceed n, giving us 0
        and stopping the calculations.
        """
        fives = 0
        
        # start with a denominator of 5
        denominator = 5
        while n >= denominator:
            # calculate how many "5" for the current
            # denominator
            fives += n // denominator
            
            # each iteration increases the power of 5
            denominator *= 5
            
        # number of 5s give us number of trailing zeroes
        return fives
