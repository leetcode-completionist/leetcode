# https://leetcode.com/problems/bulls-and-cows/
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # first find all the bulls
        bulls = 0
        
        secret_without_bulls = defaultdict(int)
        guess_without_bulls = defaultdict(int)
        
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_without_bulls[s] += 1
                guess_without_bulls[g] += 1
                
        # then find all the cows
        cows = 0
        for k, v in secret_without_bulls.items():
            cows += min(v, guess_without_bulls[k])
            
        return str(bulls) + "A" + str(cows) + "B"
