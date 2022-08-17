# https://leetcode.com/problems/unique-morse-code-words/
class Solution:
    
    ALPHABET = [
        ".-","-...","-.-.","-..",   # A-D
        ".","..-.","--.","....",    # E-H
        "..",".---","-.-",".-..",   # I-L
        "--","-.","---",".--.",     # M-P
        "--.-",".-.","...","-",     # Q-T
        "..-","...-",".--","-..-",  # U-X
        "-.--","--..",              # Y-Z
        ]
    
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        seen = set()
        
        for word in words:
            morse_code = ""
            for c in word:
                morse_code += Solution.ALPHABET[ord(c) - ord("a")]
            seen.add(morse_code)
        
        return len(seen)
