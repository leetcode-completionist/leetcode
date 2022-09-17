# https://leetcode.com/problems/longest-palindrome/
class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_map = defaultdict(int)
        for c in s:
            char_map[c] += 1
            
        res = 0       
        has_odd = False

        for v in char_map.values():
            if v % 2 == 0:
                res += v
            else:
                res += v // 2 * 2
                has_odd = True
                
        return res + (1 if has_odd else 0)
