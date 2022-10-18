# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = {}
        children = defaultdict(set)
        for i in range(n):
            parents[i] = i
            children[i].add(i)
            
        def union(a: int, b: int) -> None:
            large = parents[a]
            small = parents[b]
            if large == small:
                return
            
            if len(children[large]) < len(children[small]):
                large, small = small, large
                
            for child in children[small]:
                parents[child] = large
                children[large].add(child)
                
            del children[small]

        for a, b in edges:
            union(a, b)

        return len(children)
