# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:            
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            
            # check left-subtree is equal to right-subtree and vice-versa
            return dfs(left.right, right.left) and dfs(left.left, right.right)

        if not root:
            return True

        return dfs(root.left, root.right)
