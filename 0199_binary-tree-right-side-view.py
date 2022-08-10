# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side_view = {}
        
        def dfs(node: Optional[TreeNode], level: int) -> None:
            if not node:
                return
            
            right_side_view[level] = node.val
            
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)
            
        dfs(root, 0)
            
        res = []
        for i in range(len(right_side_view.keys())):
            res.append(right_side_view[i])
        return res
