# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], floor: int, ceil: int) -> bool:
            if not node:
                return True

            if node.val <= floor or node.val >= ceil:
                return False
            
            if node.left and not validate(node.left, floor, node.val):
                return False
            
            if node.right and not validate(node.right, node.val, ceil):
                return False
            
            return True

        return validate(root, float("-inf"), float("inf"))
