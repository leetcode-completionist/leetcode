# https://leetcode.com/problems/generalized-abbreviation/
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        
        def dfs(word: str, so_far='') -> None:
            if not word:
                res.append(so_far)
                return                           
            for i in range(len(word) + 1):
                num = str(i) if i > 0 else ""
                dfs(word[i+1:], so_far + num + word[i:i+1])

        dfs(word)
        return res
