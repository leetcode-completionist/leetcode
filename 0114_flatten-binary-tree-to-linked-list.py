# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        def dfs(node: TreeNode, l_node: TreeNode) -> TreeNode:            
            # add current node to the linkedlist
            l_node.right = node
            l_node = l_node.right
            
            # store the left and right sub-tree
            left, right = node.left, node.right
            node.left, node.right = None, None
            
            # link the left sub-tree first
            if left:
                l_node = dfs(left, l_node)
            
            # link the right sub-tree after
            if right:
                l_node = dfs(right, l_node)
            
            # return the last linkedlist node
            return l_node

        dummy = TreeNode()
        dfs(root, dummy)
