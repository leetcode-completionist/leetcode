# https://leetcode.com/problems/merge-two-binary-trees/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node1:
            return node2
        if not node2:
            return node1
        
        node = TreeNode(node1.val + node2.val)
        
        node.left = self.mergeTrees(node1.left, node2.left)
        node.right = self.mergeTrees(node1.right, node2.right)
        
        return node
