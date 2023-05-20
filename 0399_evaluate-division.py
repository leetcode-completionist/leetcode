class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(dict)
        for (left, right), val in zip(equations, values):
            d[left][right] = val
            d[right][left] = 1 / val
        
        def dfs(src: str, dst: str, seen: set[str]) -> float:
            if src in seen:
                # we already visited
                return -1.0
            
            seen.add(src)
            
            m = d[src]
            if dst in m:
                # we found our destination
                return m[dst]
            
            for k, v in m.items():
                # try each next node
                factor = dfs(k, dst, seen)
                if factor != -1.0:
                    return v * factor
            
            seen.remove(src)
            
            # no path found
            return -1.0
        
        res = []
        
        for (left, right) in queries:
            if left not in d or right not in d:
                res.append(-1.0)
                continue
                
            if left == right:
                res.append(1.0)
                continue
                
            res.append(dfs(left, right, set()))
            
        return res
