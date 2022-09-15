# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # 1 <= Node.val <= 9
        seen = [0] * 10
        
        def isPseudoPalindromic() -> bool:
            odds = 0
            for freq in seen:
                if freq % 2 != 0:
                    odds += 1
                    if odds > 1:
                        # we can have at most 1 num with odd freq
                        return False
            return True
        
        res = 0
        
        def dfs(node: TreeNode) -> None:
            nonlocal res
            
            seen[node.val] += 1
            
            if not node.left and not node.right:
                # leaf node
                if isPseudoPalindromic():
                    res += 1
            
            if node.left:
                dfs(node.left)
            
            if node.right:
                dfs(node.right)
            
            # backtrack
            seen[node.val] -= 1
        
        dfs(root)
        
        return res
