# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        if not root:
            return res
        
        def dfs(node: TreeNode) -> (int, int):
            nonlocal res
            
            # keep a maximum increasing and decreasing
            # consecutive sequence length
            max_incr, max_decr = 0, 0

            if node.left:
                # process left subtree
                incr, decr = dfs(node.left)
                
                # if we can build a consecutive sequence
                if node.val == node.left.val + 1:
                    # decreasing
                    max_decr = max(max_decr, decr)
                elif node.val == node.left.val - 1:
                    # increasing
                    max_incr = max(max_incr, incr)
                    
            if node.right:
                # process right subtree
                incr, decr = dfs(node.right)
                
                # if we can build a consecutive sequence
                if node.val == node.right.val + 1:
                    # decreasing
                    max_decr = max(max_decr, decr)
                elif node.val == node.right.val - 1:
                    # increasing
                    max_incr = max(max_incr, incr)
            
            # we check the edge case where
            # sequence go from left subtree, current node,
            # right subtree
            #
            # we don't return this up to the parent
            # because we can't build a sequence that
            # includes parent and BOTH of left/right subtrees
            #
            # instead we modify our global res variable
            res = max(res, max_incr + max_decr + 1)
            
            # we return max increasing and max decreasing
            # up to the parent
            #
            # we add one to include the current node in the
            # sequence
            return max_incr + 1, max_decr + 1
            
        dfs(root)
        
        return res
