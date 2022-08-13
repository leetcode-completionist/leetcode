class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def dfs(
            num: int,
            target: int,
            combination: List[int]) -> None:
            if len(combination) == k and target == 0:
                res.append(combination)
                return
            
            for i in range(num, 10):
                if i <= target:
                    dfs(i + 1, target - i, combination + [i])
        
        dfs(1, n, [])
        
        return res
