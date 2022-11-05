# https://leetcode.com/problems/reverse-vowels-of-a-string/
class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        
        vowels = []
        for i, c in enumerate(chars):
          if c in "aeiouAEIOU":
            vowels.append(i)
            
        l, r = 0, len(vowels) - 1
        while l < r:
          chars[vowels[l]], chars[vowels[r]] = chars[vowels[r]], chars[vowels[l]]
          l += 1
          r -= 1
        
        return "".join(chars)
