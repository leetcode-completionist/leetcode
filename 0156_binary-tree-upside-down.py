# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head = None
        
        if not root:
            return head
        
        def dfs(node: TreeNode) -> None:
            nonlocal head
            
            if not node.left:
                # we reached the left-most node
                head = node
                return
            
            # problem guarantees us that right
            # has no children
            right = node.right
            
            # remove node's pointer to right
            node.right = None
            
            # remove node's pointer to left
            left = node.left
            node.left = None
            
            dfs(left)
            
            left.left = right
            left.right = node
        
        dfs(root)
        
        return head
