# https://leetcode.com/problems/merge-strings-alternately/
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        
        use_word1 = True
        i, j = 0, 0
        
        res = ""
        while i < m and j < n:
            if use_word1:
                res += word1[i]
                i += 1
                use_word1 = False
            else:
                res += word2[j]
                j += 1
                use_word1 = True
        
        res += word1[i:]
        res += word2[j:]
        
        return res
