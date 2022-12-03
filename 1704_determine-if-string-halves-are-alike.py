# https://leetcode.com/problems/determine-if-string-halves-are-alike/
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        
        vowel_cnt = 0
        consonant_cnt = 0
        for c in s[:n//2]:
            if c in "aeiouAEIOU":
                vowel_cnt += 1
            else:
                consonant_cnt += 1
        
        for c in s[n // 2:]:
            if c in "aeiouAEIOU":
                vowel_cnt -= 1
            else:
                consonant_cnt -= 1
        
        return vowel_cnt == consonant_cnt == 0
