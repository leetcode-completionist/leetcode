# https://leetcode.com/problems/find-the-difference/
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        seen = defaultdict(int)
        for c in s:
            seen[c] += 1
            
        for c in t:
            if not seen[c]:
                return c
            else:
                seen[c] -= 1
        
        raise Exception("invalid test case")
