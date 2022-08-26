# https://leetcode.com/problems/reordered-power-of-2/
class PowersOfTwo:
    def __init__(self):
        self.counters = []
        
        n = 1
        max_n = 10 ** 9
        while n <= max_n:
            counter = [0] * 10
            for c in str(n):
                counter[int(c)] += 1
                
            self.counters.append(tuple(counter))
            n *= 2


class Solution:
    
    POWERS_OF_TWO = PowersOfTwo()
    
    def reorderedPowerOf2(self, n: int) -> bool:
        counter = [0] * 10
        for c in str(n):
            counter[int(c)] += 1
            
        tup = tuple(counter)
            
        return any(tup == p for p in Solution.POWERS_OF_TWO.counters)
