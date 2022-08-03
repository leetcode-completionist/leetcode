# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = float("-inf")
        
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal res
            
            if not node:
                return 0
            
            sum_left = max(0, dfs(node.left))
            sum_right = max(0, dfs(node.right))
            sum_sub_tree = sum_left + node.val + sum_right
            
            # check sub-tree sum before we return to a
            # higher level.
            #
            # this is because there is no way for a parent node
            # to reach both left and right subtree
            #
            # however there is a possible path from left - node - right
            res = max(res, sum_sub_tree)
            
            return max(
                node.val,
                sum_left + node.val,
                node.val + sum_right)

        dfs(root)
        
        return res
