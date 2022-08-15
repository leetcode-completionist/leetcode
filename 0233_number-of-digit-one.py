# https://leetcode.com/problems/number-of-digit-one/
class Solution:
    def countDigitOne(self, n: int) -> int:
        # count digits in one's place
        # 1, 11, 21, 31, ...
        #
        # Given n, how do we found the
        # total number of digit one in the one's
        # place? For example: 153
        #
        # First we find how many 10's we have
        # 
        #     153 // 10 = 15
        #
        # Then we find out if we have a one at
        # the 150s range (i.e. 151)
        #
        #     1 if 153 % 10 != 0 else: 0
        #
        # This returns a total of 16 ones at the
        # ones place. To verify:
        # 
        #     1, 11, 21, 31, 41, 51,
        #    61, 71, 81, 91, 101, 111,
        #   121, 131, 141, 151
        #
        # Now let's look at the 10's place.
        # Similarly, we can try the above steps:
        #
        #     153 // 100 = 1
        #         1 * 10 = 10
        #
        # We know we cover all of 0-100 range.
        # This gives us 10-19 as eligible 1's at
        # the ten's place
        #
        # What about the remaining "53"? Since 53 > 19
        # we will have:
        #
        #     10-19 (10 digits)
        #
        # What if the remaining is another number like "14"?
        #
        #     10, 11, 12, 13, 14
        #
        # The pattern here is if the number is < 10, there
        # are no more one's at the ten's place.
        #
        # If the number is >19, we automatically have ten
        # '1's at the tens place.
        #
        # We can generalize the above for any given n via:
        # any number in between will be (n - base + 1)
        # '1's at the base's place.
        #
        # An example implementation:
        res = 0

        # start at base 1
        base = 1

        while base <= n:
            divider = base * 10
            
            # first add number of ones we have at current base
            res += n // divider * base
            
            rem = n % divider
            
            if rem < base:
                # no more one's at current base
                # move our base up
                base *= 10
                continue
            elif rem >= 2 * base:
                # this means we are greater than all the one's at
                # current base (e.g. 2, 20, 200, ...)
                res += base
            else:
                # we are partially covering one's at the current base
                # (e.g. 211, 212, 2100, 2199, ...)
                res += rem - base + 1
                
            # move our base up
            base *= 10
        
        return res
