# https://leetcode.com/problems/count-univalue-subtrees/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node: TreeNode) -> (int, int, bool):
            """
            Returns the value of the node, count,
            and if node is a unival subtree to the caller.
            """
            if not node.left and not node.right:
                return (node.val, 1, True)
            
            left_val, left_subtree_count, left_is_unival = None, 0, True
            if node.left:
                left_val, left_subtree_count, left_is_unival = dfs(node.left)
                
            right_val, right_subtree_count, right_is_unival = None, 0, True
            if node.right:
                right_val, right_subtree_count, right_is_unival = dfs(node.right)
                
            # current node is a unival iff both left/right are unival and
            # current node shares the same value as both children
            node_is_unival = True
            if left_val is not None:
                node_is_unival &= (left_val == node.val and left_is_unival)
            if right_val is not None:
                node_is_unival &= (right_val == node.val and right_is_unival)
                
            unival_count = left_subtree_count + right_subtree_count
            if node_is_unival:
                unival_count += 1
                
            return (node.val, unival_count, node_is_unival)
        
        _, res, _ = dfs(root)
        
        return res
