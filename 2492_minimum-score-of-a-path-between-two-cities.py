class Node:
    def __init__(self, val: int):
        self.val = val
        self.neighbors = set()

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        nodes = {}
        
        for src, dst, dist in roads:
            if src not in nodes:
                nodes[src] = Node(val=src)
            if dst not in nodes:
                nodes[dst] = Node(val=dst)
            nodes[src].neighbors.add((dst, dist))
            nodes[dst].neighbors.add((src, dist))
            
        res = math.inf
        seen = set()

        def dfs(node: Node) -> None:
            nonlocal res
            
            if not node:
                return            
            if node.val in seen:
                return
        
            seen.add(node.val)
        
            for neighbor, dist in node.neighbors:
                res = min(dist, res)
                dfs(nodes[neighbor])
            
        dfs(nodes[1])   # start at node "1"
            
        return res
