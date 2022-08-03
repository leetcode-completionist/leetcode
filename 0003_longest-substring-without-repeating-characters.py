from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        
        freq = defaultdict(lambda: 0)
        l = 0
        r = 0
        while l < len(s):
            curr = s[r]
            freq[curr] += 1
            
            while freq[curr] > 1:
                freq[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)

            if r < len(s) - 1:
                r += 1

        return res
