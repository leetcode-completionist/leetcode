# https://leetcode.com/problems/bag-of-tokens/
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        
        score = 0
        l, r = 0, len(tokens) - 1
        while l <= r:
            left, right = tokens[l], tokens[r]
            
            if power >= left:
                # greedily play the token face up
                score += 1
                power -= left
                l += 1
            
            elif score > 0 and l < r:
                # greedily play the token face down
                score -= 1
                power += right
                r -= 1
            
            else:
                # unable to play a token, break
                break
        
        return score
