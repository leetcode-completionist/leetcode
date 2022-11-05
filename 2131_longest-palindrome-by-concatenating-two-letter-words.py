# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        sameLetters = defaultdict(int)
        diffLetters = defaultdict(int)
        for word in words:
          if word[0] == word[1]:
            sameLetters[word] += 1
          else:
            diffLetters[word] += 1
        
        pairs = 0
        
        # process words that have different letters
        for k in diffLetters.keys():
          if not diffLetters[k]:
            continue
            
          rev = k[::-1]
          
          if rev not in diffLetters:
            continue
          
          pairs += min(diffLetters[k], diffLetters[rev]) * 2
          diffLetters[rev] = 0
        
        # process words that have same letters
        center = 0
        for v in sameLetters.values():
          if v % 2 == 0:
            pairs += v
          else:
            pairs += v - 1
            center = 1
            
        return (pairs + center) * 2
