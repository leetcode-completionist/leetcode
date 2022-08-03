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
        # Morris in-order traversal
        # 
        # Keep a pointer for first and second element out of order.
        #
        # When we come across the first node out of order,
        # we automatically make the second node (first + 1)
        #
        # We will update only the second node if we come across
        # another node out of order
        first = None
        second = None
        
        # keep a pointer for last order seen during the inorder traversal
        prev = None
        node = root
        while node:
            if node.left:
                # there are left elements to be processed inorder
                t = node.left
                cycle = False
                while t.right:
                    # keep traversing to right-most leaf
                    if prev != t:
                        t = t.right
                        continue
                        
                    # we detected a cycle
                    cycle = True
                    
                    # restore the tree structure
                    t.right = None

                    # keep track of out-or-order nodes
                    if prev and node.val < prev.val:
                        if not first:
                            first = prev
                        second = node
                    
                    # we've previously gone down this left-tree
                    # hence the cycle detected. After breaking
                    # the cycle and restoring the sub-tree,
                    # current node is the latest in the inorder traversal.
                    # We will continue the traversal by going down the right
                    # subtree
                    prev = node
                    node = node.right
                    break

                if not cycle:
                    # no cycle detected, we link the right-most node
                    # back to the current node, and proceed down the
                    # left subtree
                    t.right = node                
                    node = node.left
            else:
                # no more left elements, process current node
                if prev and node.val < prev.val:
                    if not first:
                        first = prev
                    second = node
                        
                # proceed down the right subtree
                prev = node
                node = node.right

        # swap node values to restore tree
        first.val, second.val = second.val, first.val
