# https://leetcode.com/problems/permutation-in-string/
class Solution:
    def isIncluded(self, mask: List[int], seen: List[int]) -> bool:
        for i in range(26):
            if mask[i] != seen[i]:
                return False
        return True
    
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        
        if n < m: return False
        
        mask = [0] * 26
        seen = [0] * 26
        for i in range(m):
            mask[ord(s1[i]) - ord("a")] += 1
            seen[ord(s2[i]) - ord("a")] += 1
        
        for i in range(n - m):
            if self.isIncluded(mask, seen):
                return True
            
            seen[ord(s2[i + m]) - ord("a")] += 1
            seen[ord(s2[i]) - ord("a")] -= 1

        return self.isIncluded(mask, seen)
