# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        res = 0
        
        def dfs(node: TreeNode, max_so_far: int) -> None:
            nonlocal res
            
            if node.val >= max_so_far:
                res += 1
                max_so_far = node.val
            
            if node.left:
                dfs(node.left, max_so_far)
            
            if node.right:
                dfs(node.right, max_so_far)
                
        dfs(root, -math.inf)
        
        return res
