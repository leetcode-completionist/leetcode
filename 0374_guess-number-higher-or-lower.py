# https://leetcode.com/problems/guess-number-higher-or-lower/
#
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
      l, r = 1, n
      while (l <= r):
        cand = l + (r - l) // 2
        guessRes = guess(cand)
        
        if guessRes == 0:
          return cand
        elif guessRes == -1:
          r = cand - 1
        elif guessRes == 1:
          l = cand + 1
        else:
          raise Exception("invalid guess result " + str(guessRes))
          
      raise Exception("invalid test case " + str(n))
