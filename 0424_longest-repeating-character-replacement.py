# https://leetcode.com/problems/longest-repeating-character-replacement/
class Solution:
    def characterReplacement(self, s, k):
        count = defaultdict(int)
        
        res = 0
        
        max_count = 0
        
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            
            max_count = max(max_count, count[s[r]])
            
            if r - l + 1 - max_count > k:
                count[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)
            
        return res
