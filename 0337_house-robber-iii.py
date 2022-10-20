# https://leetcode.com/problems/house-robber-iii/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:        
        def dfs(node: Optional[TreeNode]) -> (int, int):            
            if not node:
                return (0, 0)
            
            include_self = node.val
            exclude_self = 0
            
            include_left, exclude_left = dfs(node.left)
            include_right, exclude_right = dfs(node.right)           
            
            max_left = max(include_left, exclude_left)
            max_right = max(include_right, exclude_right)
            
            return (include_self + exclude_left + exclude_right,
                    exclude_self + max_left + max_right)
        
        return max(dfs(root))
