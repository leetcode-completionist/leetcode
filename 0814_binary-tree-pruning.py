# https://leetcode.com/problems/binary-tree-pruning/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        def dfs(node: TreeNode) -> None:
            prune_left = prune_right = True
            
            if node.left:
                prune_left = dfs(node.left)
                if prune_left:
                    node.left = None
            
            if node.right:
                prune_right = dfs(node.right)
                if prune_right:
                    node.right = None
                    
            return prune_left and prune_right and node.val == 0
        
        prune_root = dfs(root)
        
        return root if not prune_root else None
