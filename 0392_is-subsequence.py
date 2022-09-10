# https://leetcode.com/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx, t_idx = 0, 0
        
        s_len, t_len = len(s), len(t)
        
        while s_idx < s_len and t_idx < t_len:
            if s[s_idx] == t[t_idx]:
                s_idx += 1
            t_idx += 1
            
        return s_idx == s_len
