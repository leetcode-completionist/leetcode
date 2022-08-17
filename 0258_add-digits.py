# https://leetcode.com/problems/add-digits/
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            # no way to add up digits
            return 0
        
        if num % 9 == 0:
            # the "digital root" of a non-zero num
            # is 9 if the number is divisible by 9
            return 9
        
        return num % 9
