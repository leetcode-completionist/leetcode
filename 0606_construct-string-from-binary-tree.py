# https://leetcode.com/problems/construct-string-from-binary-tree/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        def dfs(node: TreeNode) -> str:
            res = str(node.val)
            
            if node.left:
                res += "(" + dfs(node.left) + ")"
                
            if node.right:
                if not node.left:
                    res += "()"
                    
                res += "(" + dfs(node.right) + ")"
            
            return res
        
        return dfs(root)
