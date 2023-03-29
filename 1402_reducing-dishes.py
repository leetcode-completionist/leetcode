class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        
        n = len(satisfaction)
        
        @cache
        def dfs(i: int, j: int) -> int:
            if i >= n:
                return 0
            
            return max(
                satisfaction[i] * j + dfs(i + 1, j + 1),
                dfs(i + 1, j),
            )
        
        return dfs(0, 1)
