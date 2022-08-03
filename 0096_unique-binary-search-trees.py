# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def dfs(left: int, right: int) -> int:
            if left == right:
                return 0
            if left == right - 1:
                return 1

            res = 0
            for i in range(left, right):
                # count possible left sub-trees
                left_sub_trees = dfs(left, i)
                
                # count possible right sub-trees
                right_sub_trees = dfs(i + 1, right)                
                
                if right_sub_trees == 0:
                    res += left_sub_trees
                elif left_sub_trees == 0:
                    res += right_sub_trees
                else:
                    res += left_sub_trees * right_sub_trees
            return res
        
        return dfs(1, n + 1)
