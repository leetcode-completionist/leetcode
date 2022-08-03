# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_idx = 0
        
        def dfs(nums: List[int]) -> Optional[TreeNode]:
            nonlocal preorder_idx

            if not nums:
                return None
            
            node = TreeNode(val=preorder[preorder_idx])
            preorder_idx += 1
            
            i = nums.index(node.val)
            node.left = dfs(nums[:i])
            node.right = dfs(nums[i+1:])
            
            return node
        
        return dfs(inorder)
