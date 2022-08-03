# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        node = root
        prev = None
        while node:
            if not node.left:
                # no left subtree, add current
                # value to results
                res.append(node.val)
                
                # move onto the right subtree
                node = node.right
            else:
                # there is a left subtree
                prev = node.left
                while prev.right:
                    # find the right most node in
                    # the left subtree
                    prev = prev.right
                
                # link current node to the right-most node
                # in the left subtree
                prev.right = node
                
                # move node down the left-subtree
                tmp = node
                node = node.left
                tmp.left = None
            
        return res
