# https://leetcode.com/problems/find-if-path-exists-in-graph/
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        parents = {}
        
        def union(dst: int, src: int) -> int:
            dst_parent, src_parent = find(dst), find(src)
            if dst_parent != src_parent:
                parents[src_parent] = dst_parent
        
        def find(target: int) -> int:
            if target not in parents:
                parents[target] = target
                return target
            
            parent = parents[target]   
            while parents[parent] != parent:
                parent = parents[parent]
            return parent
        
        for i, (a, b) in enumerate(edges):
            union(a, b)
            
        return find(source) == find(destination)
