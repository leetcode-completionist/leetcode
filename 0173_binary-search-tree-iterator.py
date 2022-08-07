# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        # keep the top of the stack the next element
        # of the iterator.
        #
        # For inorder traversal, this will always be
        # the left most node
        node = root
        while node:
            self.stack.append(node)
            node = node.left
        

    def next(self) -> int:
        node = self.stack.pop()
        res = node.val
        
        if node.right:
            # if there is a right subtree of our
            # next element
            #
            # we will process this sub-tree first
            # before returning to a higher level
            #
            # same as before, we want to start at the
            # left most node of the sub-tree first
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        
        return res

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
