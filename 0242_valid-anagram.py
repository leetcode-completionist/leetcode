from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = defaultdict(lambda: 0)
        for c in s:
            seen[c] += 1
            
        for c in t:
            seen[c] -= 1
            
        for _, count in seen.items():
            if count:
                return False
        
        return True
