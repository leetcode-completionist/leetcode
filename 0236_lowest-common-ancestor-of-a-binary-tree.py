# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestors = []
        p_idx = -1
        q_idx = -1
        
        def dfs(node: 'TreeNode') -> bool:
            nonlocal p_idx
            nonlocal q_idx
            
            ancestors.append(node)
            if node == p:
                p_idx = len(ancestors) - 1
            if node == q:
                q_idx = len(ancestors) - 1
            
            if node.left and dfs(node.left):
                return True
            if node.right and dfs(node.right):
                return True
            
            ancestors.pop()
            if p_idx >= 0:
                p_idx = min(p_idx, len(ancestors) - 1)
            if q_idx >= 0:
                q_idx = min(q_idx, len(ancestors) - 1)
                
            return p_idx >= 0 and q_idx >= 0
            
        dfs(root)
        
        return ancestors[min(p_idx, q_idx)]
