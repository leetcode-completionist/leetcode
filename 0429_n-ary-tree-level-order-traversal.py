# https://leetcode.com/problems/n-ary-tree-level-order-traversal/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        res = []
        
        q = deque([root])
        
        while q:
            level = []
            
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                level.append(node.val)
                
                q.extend(node.children)
            
            res.append(level)
            
        return res
