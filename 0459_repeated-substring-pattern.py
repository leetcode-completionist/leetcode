class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s) // 2):
            pattern = s[0:i + 1]
            match = True
            n = len(pattern)
            j = i + 1
            while j < len(s) and (j + n) <= len(s):
                if s[j: j + n] == pattern:
                    j = j + n
                else:
                    match = False
                    break
            
            if not match:
                continue
                
            if j == len(s):
                return True
        
        return False
            
