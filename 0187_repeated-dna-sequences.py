class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        
        seen = set()
        
        for i in range(len(s) - 9):
            window = s[i:i+10]
            if window in seen:
                res.add(window)
            else:
                seen.add(window)
                
        return list(res)
