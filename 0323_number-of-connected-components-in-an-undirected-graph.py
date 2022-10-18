# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = {}
        children = defaultdict(set)
        for i in range(n):
            # initialize parents/children maps
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
                # merge smaller to larger
                parents[child] = large
                children[large].add(child)
            
            # evict "smaller" component
            del children[small]

        for a, b in edges:
            # connect components
            union(a, b)

        return len(children)
