# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
class Solution:
    def minDifficulty(self, jobDifficulties: List[int], days: int) -> int:
        n = len(jobDifficulties)
        
        @cache
        def dfs(i: int, days: int) -> int:
            if days == 0 or n - i < days:
                return -1
                
            if days == 1:
                # we can't partition any more
                return max(jobDifficulties[i:])
            
            res = math.inf
            
            curr_max = -math.inf
            for j in range(i, n - days + 1):
                # keep track of max in current "day"
                curr_max = max(curr_max, jobDifficulties[j])
                
                # keep track of min difficulty seen
                res = min(res, curr_max + dfs(j + 1, days - 1))
            
            return res
        
        return dfs(0, days)
