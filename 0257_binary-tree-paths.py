# https://leetcode.com/problems/binary-tree-paths/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        res = []
        
        def dfs(node: TreeNode, path: List[str]) -> None:
            curr_path = path + [str(node.val)]
            
            if not node.left and not node.right:
                res.append("->".join(curr_path))
                return
            
            if node.left:
                dfs(node.left, curr_path)
            
            if node.right:
                dfs(node.right, curr_path)
        
        dfs(root, [])

        return res
