# https://leetcode.com/problems/check-if-the-sentence-is-pangram/
class Solution:
    
    PANGRAM = (1 << 26) - 1    # 26 bits (a-z)
    
    def checkIfPangram(self, sentence: str) -> bool:
        mask = 0
        for c in sentence:
            mask |= 1 << (ord(c) - ord("a"))    # flip n-th bit on
            
        # check mask contains all letters
        return Solution.PANGRAM == mask
