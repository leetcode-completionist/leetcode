class Solution:
    def minOperations(self, s: str) -> int:
        # for bits at odd indices, count how many
        # ones and zeroes
        odd_zeroes, odd_ones = 0, 0
        
        # for bits at even indices, count how many
        # ones and zeros
        even_zeroes, even_ones = 0, 0
        
        for i in range(len(s)):
            bit = s[i]
            if i % 2 == 0:
                # even
                if bit == "1":
                    even_ones += 1
                else:
                    even_zeroes += 1
            else:
                # odd
                if bit == "1":
                    odd_ones += 1
                else:
                    odd_zeroes += 1
                    
        return min(
            # 0101010101 - even zeroes and odd ones
            #
            # this means we need to convert even_ones to zeroes and odd_zeroes to ones
            even_ones + odd_zeroes,

            # 1010101010 - even ones and odd zeroes
            #
            # this means we need to convert even_zeroes to ones and odd_ones to zeroes
            even_zeroes + odd_ones)
