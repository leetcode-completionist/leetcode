# https://leetcode.com/problems/determine-if-two-strings-are-close/
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_chars = [0] * 26
        word1_uniq_chars = set()
        for c in word1:
            word1_chars[ord("a") - ord(c)] += 1
            word1_uniq_chars.add(c)
        
        word2_chars = [0] * 26
        word2_uniq_chars = set()
        for c in word2:
            word2_chars[ord("a") - ord(c)] += 1
            word2_uniq_chars.add(c)
            
        if word1_uniq_chars != word2_uniq_chars:
            return False
            
        return tuple(sorted(word1_chars)) == tuple(sorted(word2_chars))
        
