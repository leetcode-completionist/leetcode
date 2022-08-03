class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort candidates so we can check for duplicate combos and prune invalid paths
        candidates.sort()
        
        # memoize results
        @cache
        def dfs(target: int) -> List[List[int]]:
            if target == 0:
                return [[]]

            res = []

            for candidate in candidates:
                if candidate > target :
                    break
                for combo in dfs(target - candidate):
                    if combo and combo[-1] < candidate:
                        continue
                    
                    # in order to make this function cache friendly
                    # we cannot mutate results from dfs calls
                    n_combo = []
                    n_combo.extend(combo)
                    n_combo.append(candidate)

                    res.append(n_combo)

            return res

        return dfs(target)
