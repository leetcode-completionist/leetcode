class Solution:

    VOWELS = 'aeiou'
    
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        
        # initial window
        for i in range(k):
            if s[i] in Solution.VOWELS:
                res += 1
        
        if res == k:
            # max num obtained
            return res
        
        left, right = 0, k - 1
        n = len(s)
        c = res
        while right < (n - 1):
            right += 1
            if s[right] in Solution.VOWELS:
                c += 1
            
            if s[left] in Solution.VOWELS:
                c -= 1
            left += 1
            
            res = max(res, c)
            
        return res
