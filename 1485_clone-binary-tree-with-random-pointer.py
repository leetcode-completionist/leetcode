# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None
        
        seen = dict()
        clone = NodeCopy()
        
        def deepCopy(src: Node, dst: NodeCopy) -> None:            
            dst.val = src.val
            seen[src] = dst
            
            if src.left is not None:
                if src.left in seen:
                    dst.left = seen[src.left]
                else:
                    dst.left = NodeCopy()
                    deepCopy(src.left, dst.left)
                
            if src.right is not None:
                if src.right in seen:
                    dst.right = seen[src.right]
                else:
                    dst.right = NodeCopy()
                    deepCopy(src.right, dst.right)
                
            if src.random is not None:
                if src.random in seen:
                    dst.random = seen[src.random]
                else:
                    dst.random = NodeCopy()
                    deepCopy(src.random, dst.random)

        deepCopy(root, clone)
        
        return clone
