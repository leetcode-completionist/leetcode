class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        
        n = len(potions)
        
        res = []
        
        for spell in spells:
            target = math.ceil(success / spell)
            if (i := bisect_left(potions, target)) < n:
                res.append(n - i)
            else:
                res.append(0)
                
        return res
