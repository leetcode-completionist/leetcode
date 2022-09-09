https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # find max attack possible, this is our max bound for bucket sort
        max_attack = 0
        for attack, defense in properties:
            max_attack = max(max_attack, attack)
            
        # initialize buckets
        max_defense = [0] * (max_attack + 2)
        
        # for each attack value, find the max defense
        for attack, defense in properties:
            max_defense[attack] = max(max_defense[attack], defense)
            
        # for each attack value (i), fill in the largest defense for
        # any attack larger than (i)
        for attack in range(max_attack - 1, -1, -1):
            max_defense[attack] = max(max_defense[attack],
                                      max_defense[attack + 1])
            
        # for each property, look up if there is a larger defense for
        # a given attack value. If so, then the property is a "weak"
        # character
        res = 0
        
        for attack, defense in properties:
            if defense < max_defense[attack + 1]:
                res += 1
                
        return res
