class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        for i, c in enumerate(s):
            # odd palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l : r + 1]
                l -= 1
                r += 1

            # even palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l : r + 1]
                l -= 1
                r += 1
                
        return res
