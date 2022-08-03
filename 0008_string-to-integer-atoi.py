class Solution:
    def myAtoi(self, s: str) -> int:
        # remove leading whitespace
        s = self.trim(s)
        
        if len(s) == 0:
            return 0
        
        # check sign
        is_negative = False
        if s[0] == "-":
            is_negative = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        
        # build result
        res = 0
        for c in s:
            if not c.isnumeric():
                break
            res *= 10
            res += int(c)
        
        # clamp integer
        if not is_negative:
            res = min(res, 2 ** 31 - 1)
        else:
            res = min(res, 2 ** 31)
        
        # apply sign
        if is_negative and res > 0:
            return -1 * res
        else:
            return res

    def trim(self, s: str) -> str:
        for i, c in enumerate(s):
            if c == " ":
                continue
            return s[i:]
        return ""
