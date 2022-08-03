class Solution:
    
    SYMBOLS = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }
    
    def romanToInt(self, s: str) -> int:
        res = 0

        buf = ""
        for c in s[::-1]:
            n_buf = c + buf
            if n_buf not in Solution.SYMBOLS:
                # flush buffer to res
                res += Solution.SYMBOLS[buf]
                buf = c
            else:
                # buffer roman numerals until invalid
                buf = n_buf
        
        # flush buffer to res
        res += Solution.SYMBOLS[buf]
            
        return res
