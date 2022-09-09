# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # first sort by attack in decreasing order
        # then by defense in increasing order
        properties.sort(key = lambda x: (-x[0], x[1]))
        
        res = 0
        max_defense = 0
        
        # as we iterate through the attacks (in decreasing order)
        # if we see a lower defense than our max, we know we have a 
        # "weak" character.
        #
        # then we always make sure to keep track of the max defense possible
        for attack, defense in properties:
            if max_defense > defense:
                res += 1
            max_defense = max(defense, max_defense)
        
        return res
