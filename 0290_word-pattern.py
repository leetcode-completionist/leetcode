# https://leetcode.com/problems/word-pattern/
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        
        if len(pattern) != len(words):
            return False
        
        c_to_word = {}
        word_to_c = {}
        
        for c, word in zip(pattern, words):
            if c not in c_to_word and word not in word_to_c:
                c_to_word[c] = word
                word_to_c[word] = c
            
            elif c not in c_to_word:
                return False
            
            elif word not in word_to_c:
                return False
            
            elif c_to_word[c] != word or word_to_c[word] != c:
                return False
            
        return True
