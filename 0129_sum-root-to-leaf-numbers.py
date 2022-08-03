# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: Optional[TreeNode]) -> List[str]:
            if not node:
                return []
            if not node.left and not node.right:
                return [str(node.val)]
            
            res = dfs(node.left) + dfs(node.right)
            
            return [str(node.val) + r for r in res]
        
        res = 0
        for num in dfs(root):
            res += int(num)
    
        return res
