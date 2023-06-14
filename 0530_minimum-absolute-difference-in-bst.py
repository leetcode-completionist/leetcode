import math

from typing import Tuple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = math.inf
        
        def inorder(node: TreeNode) -> Tuple[int, int]:
            nonlocal res
            
            ret_min = ret_max = node.val
            
            if node.left:
                ret_min, left_max = inorder(node.left)
                res = min(res, node.val - left_max)

            if node.right:
                right_min, ret_max = inorder(node.right)
                res = min(res, right_min - node.val)
                
            return (ret_min, ret_max)
                
                
        _, _ = inorder(root)
        
        return res
        
