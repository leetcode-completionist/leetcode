class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        morph = {}
        morph_back = {}
        for i in range(len(s)):
            if s[i] not in morph and t[i] not in morph_back:
                morph[s[i]] = t[i]
                morph_back[t[i]] = s[i]
            elif s[i] not in morph or t[i] not in morph_back:
                return False
            elif morph[s[i]] != t[i] or morph_back[t[i]] != s[i]:
                return False
                
        return True
