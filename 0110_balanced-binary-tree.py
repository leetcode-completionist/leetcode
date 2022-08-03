# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> (int, bool):
            """
            Given a node, return a tuple.
            
            The first value is the max depth at this node.
            
            The second value is whether or not this node
            is a balanced binary tree.
            """
            if not node:
                return (0, True)
            
            left_h, left_balanced = dfs(node.left)
            right_h, right_balanced = dfs(node.right)

            return (max(left_h, right_h) + 1,
                    abs(left_h - right_h) <= 1 and
                    left_balanced and right_balanced)
        
        return dfs(root)[-1]
