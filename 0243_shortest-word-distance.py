# https://leetcode.com/problems/shortest-word-distance/
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        res = math.inf

        p1, p2 = None, None        
        for i, word in enumerate(wordsDict):
            if word != word1 and word != word2:
                continue

            if word == word1:
                p1 = i
            elif word == word2:
                p2 = i
            
            if p1 is not None and p2 is not None:
                res = min(res, abs(p1 - p2))

        return res
