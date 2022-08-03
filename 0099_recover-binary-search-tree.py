# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorder = []
        
        def dfs(node: Optional[TreeNode]) -> None:
            if not node: return
            dfs(node.left)
            inorder.append(node)
            dfs(node.right)

        dfs(root)
        
        sort = sorted(node.val for node in inorder)
        
        for i in range(len(sort)):
            inorder[i].val = sort[i]
