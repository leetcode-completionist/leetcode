https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        mismatched_s1 = ""
        mismatched_s2 = ""
        
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                mismatched_s1 += c1
                mismatched_s2 += c2
        
        if len(mismatched_s1) != 2:
            # no possible to match with one swap
            return False
        
        return mismatched_s1[0] == mismatched_s2[1] and mismatched_s2[0] == mismatched_s1[1]
