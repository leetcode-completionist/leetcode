# https://leetcode.com/problems/sum-of-number-and-its-reverse/
class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num, num // 2 - 1, -1):
            i_s = str(i)
            i_s_n = len(i_s)
            
            diff = num - i
            diff_s = str(diff).zfill(i_s_n)
            
            if i_s[::-1] == diff_s:
                return True
        
        return False
