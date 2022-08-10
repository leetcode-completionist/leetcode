class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n not in seen:
            seen.add(n)
            
            digits = list(str(n))
            n = sum([int(digit) ** 2 for digit in digits])
            
            if n == 1:
                return True
            
        return False
