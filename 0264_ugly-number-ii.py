# https://leetcode.com/problems/ugly-number-ii/
class Ugly:
    def __init__(self):
        self.dp = [0] * 1690
        self.dp[0] = 1
        
        t1 = t2 = t3 = 0

        for i in range(1, 1690):
            # we have to get ugly numbers 1690th times
            # and we need them in increasing order
            #
            # an ugly number can only be generated from
            # another ugly number (i.e. n*2, n*3, n*5)
            # 
            # however, we can't just multiply and add nums
            # because we care about the ordering of all possible
            # ugly numbers (e.g. n*6, n*20, etc)
            #
            # as a result, we check all possible next
            # nums by multiplying each multiple where they
            # were last seen and finding the smallest num.
            #
            # then we advance our pointer for the corresponding
            # multiplier
            self.dp[i] = min(self.dp[t1] * 2,
                             self.dp[t2] * 3,
                             self.dp[t3] * 5)
            
            if(self.dp[i] == self.dp[t1] * 2):
                t1 += 1
            if(self.dp[i] == self.dp[t2] * 3):
                t2 += 1
            if(self.dp[i] == self.dp[t3] * 5):
                t3 += 1

                
class Solution:
    
    # static instance of precomputed ugly numbers
    UGLY = Ugly()
    
    def nthUglyNumber(self, n: int) -> int:
        return Solution.UGLY.dp[n - 1]
