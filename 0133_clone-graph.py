"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        seen = {}
        
        def dfs(node: 'Node') -> 'Node':
            if node in seen:
                # already visited
                return seen[node]
            
            clone = Node(val=node.val)
            seen[node] = clone
            
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
                
            return clone
        
        return dfs(root)
