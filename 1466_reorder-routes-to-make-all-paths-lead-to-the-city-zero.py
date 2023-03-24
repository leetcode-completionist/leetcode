class Node:
    def __init__(self, id: int):
        self.id = id
        self.in_nodes = set()
        self.out_nodes = set()

        
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        nodes = [None] * n
        for a, b in connections:
            if nodes[a] is None:
                nodes[a] = Node(id=a)
            if nodes[b] is None:
                nodes[b] = Node(id=b)
            nodes[a].out_nodes.add(nodes[b])
            nodes[b].in_nodes.add(nodes[a])

        seen = set()
        res = 0       
        def dfs(node: Node) -> None:
            nonlocal res            
            seen.add(node.id)
            
            for nextNode in node.in_nodes:
                if nextNode.id not in seen:
                    dfs(nextNode)
            
            for nextNode in node.out_nodes:
                if nextNode.id not in seen:
                    res += 1
                    dfs(nextNode)
            
        dfs(nodes[0])   # start at city 0
        
        return res
