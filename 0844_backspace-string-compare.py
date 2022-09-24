# https://leetcode.com/problems/backspace-string-compare/
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def buildString(s: str) -> str:
            res = ""
            for c in s:
                if c == "#":
                    res = res[:len(res) - 1]
                else:
                    res += c
            return res
        
        return buildString(s) == buildString(t)
