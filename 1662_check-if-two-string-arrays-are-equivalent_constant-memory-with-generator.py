# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def generate(word: List[str]) -> str:
            for w in word:
                for c in w:
                    yield c
            yield None
            
        for a, b in zip(generate(word1), generate(word2)):
            if a != b:
                return False
        
        return True
