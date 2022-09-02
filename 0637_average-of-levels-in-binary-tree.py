# https://leetcode.com/problems/average-of-levels-in-binary-tree/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        res = []
        
        q = deque([root])
        while q:
            total, count = 0, 0
            
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                total += node.val
                count += 1
            
            res.append(total / count)
        
        return res
