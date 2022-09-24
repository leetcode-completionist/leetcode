# https://leetcode.com/problems/decode-string/
class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack = []
        
        for c in s:
            if c.isdigit():
                if stack and isinstance(stack[-1], int):
                    stack[-1] *= 10
                    stack[-1] += int(c)
                else:
                    stack.append(int(c))
                    
            elif c == "[":
                stack.append(c)
                
            elif c == "]":
                frag = ""
                while stack[-1] != "[":
                    frag = stack.pop() + frag
                
                stack.pop() # pop "["
                freq = stack.pop() # pop digit
                
                stack.append(frag * freq)
            else:
                stack.append(c)
                
        while stack:
            res = stack.pop() + res
        
        return res
