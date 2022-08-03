# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def clone(node: Optional[TreeNode]) -> Optional[TreeNode]:
            # deep copy of a given tree
            if not node:
                return None
            copy = TreeNode(val=node.val)
            copy.left = clone(node.left)
            copy.right = clone(node.right)
            return copy
        
        @cache
        def dfs(left: int, right: int) -> List[Optional[TreeNode]]:
            if left == right:
                return []
            if left == right - 1:
                return [TreeNode(val=left)]

            res = []
            
            for i in range(left, right):
                # generate all possible left sub-trees
                left_sub_trees = dfs(left, i)
                
                # generate all possible right sub-trees
                right_sub_trees = dfs(i + 1, right)                
                
                if left_sub_trees and not right_sub_trees:
                    for left_sub_tree in left_sub_trees:
                        root = TreeNode(val=i)
                        root.left = clone(left_sub_tree)
                        res.append(root)

                elif not left_sub_trees and right_sub_trees:
                    for right_sub_tree in right_sub_trees:
                        root = TreeNode(val=i)
                        root.right = clone(right_sub_tree)
                        res.append(root)
                else:
                    for left_sub_tree in left_sub_trees:
                        for right_sub_tree in right_sub_trees:
                            root = TreeNode(val=i)
                            root.left = clone(left_sub_tree)
                            root.right = clone(right_sub_tree)
                            res.append(root)

            return res
        
        return dfs(1, n + 1)
