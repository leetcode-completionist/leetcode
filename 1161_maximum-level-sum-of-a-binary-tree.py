import math

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = [
            -1,         # level
            -math.inf,  # sum
        ]
        
        q = deque([root])
        level = 1
        while q:
            n = len(q)
            level_sum = 0
            for _ in range(n):
                node = q.popleft()
                level_sum += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if level_sum > res[1]:
                res[0] = level
                res[1] = level_sum
                
            level += 1
        
        return res[0]
