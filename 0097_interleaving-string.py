class Solution:
    @cache
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        if not s1 and not s2 and not s3:
            return True
        
        if not s3:
            return False
        
        if s1 and s1[0] == s3[0] and self.isInterleave(s1[1:], s2, s3[1:]):
            return True
        
        if s2 and s2[0] == s3[0] and self.isInterleave(s1, s2[1:], s3[1:]):
            return True
        
        return False
