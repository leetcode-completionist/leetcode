# https://leetcode.com/problems/leaf-similar-trees/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:        
        def leafSequence(node: Optional[TreeNode], seq: List[int]):
            if not node:
                return
            if not node.left and not node.right:
                seq.append(node.val)
                return
            if node.left:
                leafSequence(node.left, seq)
            if node.right:
                leafSequence(node.right, seq)
                
        seq1 = []
        leafSequence(root1, seq1)
        
        seq2 = []
        leafSequence(root2, seq2)
        
        return tuple(seq1) == tuple(seq2)
