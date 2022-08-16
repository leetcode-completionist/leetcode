# https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dup = set()
        seen = {}
        
        for i, c in enumerate(s):
            if c in dup:
                continue
            elif c in seen:
                dup.add(c)
                del seen[c]
            else:
                seen[c] = i
                
        if not seen:
            return -1
        
        return min(seen.values())
