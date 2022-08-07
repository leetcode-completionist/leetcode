class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        if numerator == denominator:
            return "1"
        
        is_positive = (numerator < 0) == (denominator < 0)
        
        res = ""
        if not is_positive:
            res += "-"
        
        dividend = abs(numerator)
        divisor = abs(denominator)
        
        # handle left of decimal
        quotient = dividend // divisor
        res += str(quotient)
        dividend -= quotient * divisor
        
        if not dividend:
            # divisor divides perfectly without remainder
            # we are done
            return res
        
        # start handling right of decimal
        res += "."
        
        # a buffer to hold the decimal portion of the quotient
        decimals = []
        
        # maps a dividend of a division step to
        # the index of its quotient within the decimal buffer
        #
        # this lets us know when we will enter a division loop
        dividend_to_decimal_idx = {}

        # keep dividing until we terminate (e.g. dividend is 0)
        # or we detect repeating decimals
        repeating = -1
        while dividend > 0:
            dividend *= 10
            if dividend < divisor:
                # dividend is still too small, try again with one more
                # decimal place to the right
                decimals.append("0")
                continue
            
            if dividend in dividend_to_decimal_idx:
                # we have tried division with this dividend before
                # this means we will enter a loop
                repeating = dividend_to_decimal_idx[dividend]
                break
            
            quotient = dividend // divisor            
            decimals.append(str(quotient))
            
            # keep track of where a possible
            # repeating decimal can start
            dividend_to_decimal_idx[dividend] = len(decimals) - 1
            
            dividend -= quotient * divisor
            
        if repeating < 0:
            # no repeating decimals detected
            return res + "".join(decimals)
        
        return (res +
                "".join(decimals[:repeating]) +
                "(" + "".join(decimals[repeating:]) + ")")
