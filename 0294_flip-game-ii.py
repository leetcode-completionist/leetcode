# https://leetcode.com/problems/flip-game-ii/
class Solution:
    @cache
    def canWin(self, currentState: str) -> bool:
        for i in range(len(currentState) - 1):
            # for each possible move, check if next move can win
            if currentState[i:i + 2] == '++':
                
                nextState = currentState[:i] + '--' + currentState[i + 2:]
                if not self.canWin(nextState):
                    # next move cannot win
                    # this means our current move will guarantee a win
                    return True
                  
        # tried all moves but no guarantee win
        return False
