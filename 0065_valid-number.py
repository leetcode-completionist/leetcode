class Solution:
    def isNumber(self, s: str) -> bool:
        e_index = -1
        for i, c in enumerate(s):
            if c == "e" or c == "E":
                if e_index > 0:
                    # there can only be 1 "e"
                    return False
                else:
                    e_index = i       
        
        if e_index == -1:
            # drop any optional sign
            s = self.dropSign(s)
            
            # no "e", validate s is either a decimal number or an integer
            return self.isDecimalNumber(s) or self.isInteger(s)
            
        left = s[:e_index]
        right = s[e_index + 1:]

        # drop any optional signs:
        left = self.dropSign(left)
        right = self.dropSign(right)
        
        # str to the left of "e" must be either decimal or integer
        # str to the right of "e" must be an integer
        return (self.isDecimalNumber(left) or self.isInteger(left)) and self.isInteger(right)
        
        
    def isDecimalNumber(self, s: str) -> bool:
        if not s:
            return False
        
        # a decimal number has exactly 1 dot and at least 1 digit
        has_dot = False
        has_digit = False
        
        for c in s:
            if c == ".":
                if has_dot:
                    # there can only be 1 dot
                    return False
                else:
                    has_dot = True
            elif c.isnumeric():
                if not has_digit:
                    has_digit = True
            else:
                # invalid chars
                return False

        return has_dot and has_digit
        
        
    def isInteger(self, s: str) -> bool:
        if not s:
            return False
        for c in s:
            if not c.isnumeric():
                return False
        return True
    
    
    def dropSign(self, s: str) -> str:
        if s and (s[0] == "+" or s[0] == "-"):
            return s[1:]
        return s
