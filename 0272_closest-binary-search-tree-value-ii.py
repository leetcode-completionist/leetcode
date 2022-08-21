# https://leetcode.com/problems/closest-binary-search-tree-value-ii/
import heapq

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        heap = []
        
        def dfs(node: TreeNode) -> None:
            heapq.heappush(heap, (abs(node.val - target), node.val))
            
            if node.left:
                dfs(node.left)
            
            if node.right:
                dfs(node.right)
        
        dfs(root)
        
        res = []
        while heap and len(res) < k:
            res.append(heapq.heappop(heap)[-1])
        
        return res
