class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not k:
            return 0
        
        i = j = 0
        seen = { s[i]: 1 }
        n = len(s)
        res = 1
        
        while j < (n - 1):
            j += 1
            a, b = s[i], s[j]
            
            if b in seen:
                seen[b] += 1
                res = max(res, j - i + 1)
                continue
            
            while len(seen) >= k:
                c = s[i]
                seen[c] -= 1
                if seen[c] == 0:
                    del seen[c]
                i += 1
                    
            seen[b] = 1
            res = max(res, j - i + 1)
        
        return res
