# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        height = -1
        
        # find the lowest level
        node = root
        while node:
            height += 1
            node = node.left
            
        if height == 0:
            # only one level (i.e. root)
            return 1

        # given an index to a leaf node in the bottom row
        # and the l, r bounds, we will traverse from
        # root down to the index to see if the leaf node
        # exists
        def hasNode(idx) -> bool:
            l, r = 0, 2 ** height - 1
            node = root
            
            for _ in range(height):
                mid = l + (r - l) // 2
                
                if idx <= mid:
                    node = node.left
                    r = mid
                else:
                    node = node.right
                    l = mid + 1
            
            return node is not None
        
        # perform binary search to find the first
        # missing leaf node
        #
        # then we will know how many leaf nodes there
        # are in the tree
        l, r = 0, 2 ** height - 1
        while l <= r:
            mid = l + (r - l) // 2
            
            if hasNode(mid):
                # look to the right
                l = mid + 1
            else:
                # look to the left
                r = mid - 1
        
        return (2 ** height - 1) + l
