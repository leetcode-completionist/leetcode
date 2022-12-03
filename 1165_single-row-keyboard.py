# https://leetcode.com/problems/single-row-keyboard/
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        indices = {}
        for i, key in enumerate(keyboard):
            indices[key] = i
        
        res = 0
        cur = 0
        for c in word:
            i = indices[c]
            res += abs(i - cur)
            cur = i
        return res
