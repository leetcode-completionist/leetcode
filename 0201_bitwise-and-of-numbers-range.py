class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Bitwise AND only returns true if two bits are both
        # '1's
        #
        # The trick to this problem is that we need to find
        # common prefixes between left and right.
        #
        # The reason being that beyond the common prefixes,
        # there will be at least one number in the range that
        # does not share a bit with all other numbers.
        #
        # However, ALL numbers in the range will share any
        # common prefixes between left and right.
        l_b = "{:032b}".format(left)
        r_b = "{:032b}".format(right)
        
        res_b = ""
        for i in range(len(l_b)):
            if l_b[i] != r_b[i]:
                # no longer common prefix, break out
                break
            res_b += l_b[i]
        
        # pad the resulting string with zeroes
        # because we know these can't be '1'
        res_b += "0" * (len(l_b) - len(res_b))
        
        return int(res_b, 2)
