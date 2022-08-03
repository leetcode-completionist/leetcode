class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # start with 1 in the carry to kick things off
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            s = digits[i] + carry
            c = s % 10
            digits[i] = c
            if s == c:
                # no carry, we are done!
                return digits
        # we still have a carry, prepend 1
        return [1] + digits
