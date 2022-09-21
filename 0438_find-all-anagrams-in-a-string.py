# https://leetcode.com/problems/find-all-anagrams-in-a-string/
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        requirement = [0] * 26
        for c in p:
            requirement[ord(c) - ord("a")] += 1
        requirement = tuple(requirement)
        
        seen = [0] * 26
        for i in range(len(p)):
            seen[ord(s[i]) - ord("a")] += 1
        
        l, r = 0, len(p) - 1
        res = []
        while r < len(s) - 1:
            if tuple(seen) == requirement:
                res.append(l)
            
            r += 1
            seen[ord(s[r]) - ord("a")] += 1
            seen[ord(s[l]) - ord("a")] -= 1
            l += 1
        
        if tuple(seen) == requirement:
                res.append(l)
        return res
