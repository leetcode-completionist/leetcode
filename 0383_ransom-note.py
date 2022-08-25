# https://leetcode.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available = defaultdict(int)
        for c in magazine:
            available[c] += 1
            
        for c in ransomNote:
            available[c] -= 1
            if available[c] < 0:
                return False
            
        return True
