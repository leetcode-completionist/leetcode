class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            # verify that there are enough gas
            return -1
        
        total = 0
        res = -1
        
        for i, (g, c) in enumerate(zip(gas, cost)):
            total += g - c
            if total >= 0 and res == -1:
                # tank is enough to get us to the next step
                # update our result to current index if
                # it is not already set
                res = i
            elif total < 0:
                # tank drops below zero, no longer possible
                # to complete the circuit, reset result to
                # -1
                total = 0
                res = -1
        
        return res
