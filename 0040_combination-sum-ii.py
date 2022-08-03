class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def dfs(candidates: List[int], target: int) -> List[List[int]]:
            if target == 0:
                return [[]]
            
            res = []
            
            for i, c in enumerate(candidates):
                if i > 0 and c == candidates[i - 1]:
                    # we've already tried this candidate
                    continue
                if c > target:
                    # too big to sum up to target
                    continue
                
                combos = dfs(candidates[i + 1:], target - c)
                for combo in combos:
                    combo.append(c)
                    res.append(combo)
                    
            return res
        
        return dfs(candidates, target)
