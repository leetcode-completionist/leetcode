# https://leetcode.com/problems/string-compression-ii/
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        
        @cache
        def dfs(i: int,
                last_char: str,
                last_char_count: int,
                k: int) -> int:
            if k < 0: 
                return math.inf
            if i == n:
                return 0
            
            delete_char = dfs(
                i + 1,
                last_char,
                last_char_count,
                k - 1)
            
            if s[i] == last_char:
                keep_char = dfs(i + 1, last_char, last_char_count + 1, k)
                if last_char_count in [1, 9, 99]:
                    # increase count by one
                    keep_char += 1
            else:
                keep_char = dfs(i + 1, s[i], 1, k) + 1
                
            return min(delete_char, keep_char)
        
        return dfs(0, "", 0, k)
