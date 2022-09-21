# https://leetcode.com/problems/sum-of-left-leaves/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = 0
        
        def dfs(node: TreeNode, is_left: bool) -> None:
            nonlocal res
            
            if not node.left and not node.right:
                if is_left:
                    res += node.val
                return
            
            if node.left:
                dfs(node.left, True)
            
            if node.right:
                dfs(node.right, False)
                
        dfs(root, False)
        
        return res
