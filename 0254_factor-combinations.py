# https://leetcode.com/problems/factor-combinations/
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def dfs(start: int, n: int) -> List[List[int]]:
            # we don't need to look past sqrt(n) since
            # mathematically two factors cannot BOTH be
            # greater than sqrt(n)
            limit = int(math.sqrt(n))
            
            res = []
            
            for i in range(start, limit + 1):
                if n % i == 0:
                    # we found a factor
                    res.append([i, n // i])

                    # get all possible sub-factors
                    for r in dfs(i, n // i):
                        res.append([i] + r)
        
            return res
        
        return dfs(2, n)
