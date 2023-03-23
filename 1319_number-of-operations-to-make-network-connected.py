from typing import Set

class Node:
    def __init__(self, id: int):
        self.id = id
        self.neighbors = set()

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if (n - 1) > len(connections):
            # Not enough cables.
            return -1
        
        # Build graph
        remaining_ids = set([i for i in range(n)])
        nodes = {}
        for a, b in connections:
            if a not in nodes:
                nodes[a] = Node(id = a)
            if b not in nodes:
                nodes[b] = Node(id = b)
            nodes[a].neighbors.add(nodes[b])
            nodes[b].neighbors.add(nodes[a])
            remaining_ids.discard(a)
            remaining_ids.discard(b)
        for remaining in remaining_ids:
            nodes[remaining] = Node(id = remaining)
        
        # Recursive DFS
        def dfs(node: Node, seen: Set[int]) -> None:
            if node.id in seen:
                return
            seen.add(node.id)
            if node.id in nodes:
                nodes.pop(node.id)
            for neighbor in node.neighbors:
                dfs(neighbor, seen)
        
        clusters = 0
        while nodes:
            dfs(nodes.popitem()[-1], set())
            clusters += 1
        return clusters - 1
