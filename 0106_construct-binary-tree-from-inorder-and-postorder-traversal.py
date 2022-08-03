# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postorder_idx = len(postorder) - 1
        
        def dfs(nums: List[int]) -> Optional[TreeNode]:
            nonlocal postorder_idx

            if not nums:
                return None
            
            node = TreeNode(val=postorder[postorder_idx])
            postorder_idx -= 1
            
            i = nums.index(node.val)
            node.right = dfs(nums[i+1:])
            node.left = dfs(nums[:i])
            
            return node
        
        return dfs(inorder)
