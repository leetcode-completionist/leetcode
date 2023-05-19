from collections import defaultdict

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:                
        nodes = {}
        visited = [False] * len(graph)
        
        def dfs(prev_state: bool, node: int) -> bool:
            new_state = not prev_state
            
            if node in nodes:
                return nodes[node] == new_state
        
            nodes[node] = new_state
            
            for neighbor in graph[node]:
                if not dfs(new_state, neighbor):
                    return False
            
            return True
        
        for i in range(len(graph)):
            if i not in nodes:
                if not dfs(True, i):
                    return False
        
        return True
