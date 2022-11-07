# https://leetcode.com/problems/maximum-69-number/
class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))
        
        for i, c in enumerate(s):
            if c == "6":
                return int("".join(s[:i]) + "9" + "".join(s[i + 1:]))
        
        return num
