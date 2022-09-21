# https://leetcode.com/problems/letter-case-permutation/
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if not s:
            return []
        
        prefix = []
        
        c = s[0]
        prefix.append(c)
        if ord(c) >= ord("a"):
            prefix.append(c.upper())
        elif ord(c) >= ord("A"):
            prefix.append(c.lower())
                       
        suffix = self.letterCasePermutation(s[1:])
            
        if not suffix:
            return prefix
            
        res = []
        for pre in prefix:
            for suf in suffix:
                res.append(pre + suf)
        return res
