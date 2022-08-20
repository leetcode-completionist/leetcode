# https://leetcode.com/problems/minimum-number-of-refueling-stops/
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        
        dp = [startFuel] + [0] * n
        
        for i in range(n):
            pos, fuel = stations[i]
            
            for j in range(i, -1, -1):
                # we revisit all the steps we have calculated so far
                if dp[j] >= pos:
                    # we can reach the current station with j steps
                    # so we will use current station's fuel to see
                    # how far we can go
                    dp[j + 1] = max(dp[j + 1], dp[j] + fuel)
        
        # search each number of stops to see when's the earliest
        # we can reach our target
        for i in range(len(dp)):
            if dp[i] >= target:
                return i
            
        # we weren't able to find a number of stops that will
        # get us to the target
        return -1
