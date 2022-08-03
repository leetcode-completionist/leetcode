class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # positive if both are same sign
        is_positive = (dividend < 0) == (divisor < 0)
        
        dividend, divisor = abs(dividend), abs(divisor)

        res = 0
        
        while dividend >= divisor:
            # iteratively subtract a doubling divisor
            # restart with original divisor if temp_divisor gets too big
            temp_divisor, count = divisor, 1
            while dividend >= temp_divisor:
                dividend -= temp_divisor
                res += count

                # double temp_divisor and count
                temp_divisor += temp_divisor
                count += count

        # clamp results
        if not is_positive:
            if res > (2 ** 31):
                res = 2 ** 31
            res = -res
        else:
            if res > (2 ** 31) - 1:
                res = 2 ** 31 - 1

        return res
