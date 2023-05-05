class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        banned = set()
        
        n = len(senate)
        r = d = 0
        for c in senate:
            if c == 'R':
                r += 1
            elif c == 'D':
                d += 1
        
        while r and d:
            for i, c in enumerate(senate):
                if i in banned:
                    continue
                
                if not r or not d:
                    # only 1 party left
                    break
                    
                if c == 'R':
                    # ban the next D
                    j = (i + 1) % n
                    while j != i:
                        if senate[j] != 'R' and j not in banned:
                            banned.add(j)
                            break
                        j += 1
                        j %= n
                    d -= 1
                    
                elif c == 'D':
                    # ban the next R
                    j = (i + 1) % n
                    while j != i:
                        if senate[j] != 'D' and j not in banned:
                            banned.add(j)
                            break
                        j += 1
                        j %= n                    
                    r -= 1
                    
                else:
                    raise Exception('invalid party \'{}\''.format(c))
            
        if r:
            return 'Radiant'
        else:
            return 'Dire'
        
