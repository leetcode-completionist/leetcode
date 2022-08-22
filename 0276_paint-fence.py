# https://leetcode.com/problems/paint-fence/
class Solution:
    def numWays(self, n: int, k: int) -> int:        
        @cache
        def dfs(fence_remaining: int) -> int:            
            if fence_remaining == 1:
                # base case
                return k
            
            if fence_remaining == 2:
                # base case
                return k * k
            
            # we can paint UP TO two fences with
            # the same color
            #
            # at every DFS call, we will paint 1 or 2 fences
            # with the same color.
            #
            # every time we paint a fence, we have (k - 1) possible
            # colors to choose from.
            #
            # since we only care about # of possibilities
            # we will multiply the possibilities to get our results
            return (k - 1) * (dfs(fence_remaining - 1) +
                              dfs(fence_remaining - 2))
        
        return dfs(n)
