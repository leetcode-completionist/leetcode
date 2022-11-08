# https://leetcode.com/problems/make-the-string-great/
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack:
                if c.isupper() and stack[-1] == c.lower():
                    stack.pop()
                    continue
                elif c.islower() and stack[-1] == c.upper():
                    stack.pop()
                    continue
            stack.append(c)
        return "".join(stack)
