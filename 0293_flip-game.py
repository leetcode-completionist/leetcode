# https://leetcode.com/problems/flip-game/
class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        n = len(currentState)
        
        if n < 2:
            return []
        
        res = []
        
        for i in range(n - 1):
            if currentState[i:i+2] == "++":
                res.append(currentState[:i] + "--" + currentState[i + 2:])
            
        return res
