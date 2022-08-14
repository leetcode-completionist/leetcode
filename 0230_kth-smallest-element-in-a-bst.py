# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node: TreeNode) -> Optional[int]:
            nonlocal k
            
            if node.left:
                res = dfs(node.left)
                if res is not None:
                    return res
            
            k -= 1
            
            if not k:
                return node.val
            
            if node.right:
                return dfs(node.right)

        return dfs(root)
