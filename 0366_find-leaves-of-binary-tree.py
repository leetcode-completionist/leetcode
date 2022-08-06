# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        leaf_levels = defaultdict(list)
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            
            if not node.left and not node.right:
                # first leaf level found
                leaf_levels[0].append(node.val)
                return 0
            
            # we choose the higher of the two
            # because this node cannot become a leaf
            # until BOTH children are removed
            curr_level = max(dfs(node.left), dfs(node.right)) + 1            
            leaf_levels[curr_level].append(node.val)
            return curr_level
        
        dfs(root)
        
        return leaf_levels.values()
