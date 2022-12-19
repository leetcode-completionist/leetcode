# https://leetcode.com/problems/range-sum-of-bst/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        
        def dfs(node: Optional[TreeNode]) -> None:
          nonlocal res
          
          if not node:
            return
          
          if low <= node.val <= high:
            res += node.val
          
          if node.val <= high:
            dfs(node.right)
          
          if node.val >= low:
            dfs(node.left)
        
        dfs(root)
        
        return res
