# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        bitmasks = []
        for s in arr:
            if len(s) != len(set(s)):
                # string contains duplicated letters
                # invalid for concantenation
                continue
            mask = 0
            for c in s:
                mask |= 1 << (ord(c) - ord("a"))
            bitmasks.append(mask)
            
        n = len(bitmasks)
        
        def dfs(i: int, seen: int) -> int:
            if i == n:
                return bin(seen).count("1")
            
            res = 0
            mask = bitmasks[i]
            if ~seen & mask == mask:
                # all bits not seen yet
                res = dfs(i + 1, seen | mask)
            
            return max(res, dfs(i + 1, seen))
              
        return dfs(0, 0)
