# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # we know we have at least one node
        res = 1
        
        def dfs(node: TreeNode, prev: int, streak: int) -> None:
            nonlocal res
            
            if node.val == prev + 1:
                streak += 1
            else:
                streak = 1
            
            res = max(res, streak)
                
            if node.left:
                dfs(node.left, node.val, streak)
            
            if node.right:
                dfs(node.right, node.val, streak)
        
        dfs(root, -math.inf, 0)
        
        return res
