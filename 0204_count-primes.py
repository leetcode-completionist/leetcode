class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            # question asks for strictly
            # less than n
            return 0
        
        # 0 is not a prime
        # 1 is not a prime
        #
        # we initialize everything else as prime
        # for now
        sieve = [False, False] + [True] * (n - 2)
        
        for i in range(2, math.ceil(math.sqrt(n))):
            # We only need to check up to sqrt because
            # If a number n is not a prime, it can be
            # factored into two factors a and b:
            #
            # n = a * b
            # 
            # a and b can't be both greater than the square root of n.
            # So in any factorization of n, at least one of the factors
            # must be smaller than the square root of n, and if we can't
            # find any factors less than or equal to the square root,
            # n must be a prime.
            if sieve[i]:
                # set all multiples of i to false
                # because they are not prime
                for multiple in range(i*i, n, i):
                    sieve[multiple] = False
                    
        # return total number of values that are
        # True (i.e. prime)
        return sum(sieve)
