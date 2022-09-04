# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
from functools import cmp_to_key

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = defaultdict(list)
        
        q = deque([(root, 0, 0)])
        
        # perform BFS and fill up each level (i.e. col)
        while q:
            n = len(q)
            for _ in range(n):
                node, row, col = q.popleft()
                levels[col].append((node.val, row))
                
                if node.left:
                    q.append((node.left, row + 1, col - 1))
                    
                if node.right:
                    q.append((node.right, row + 1, col + 1))
                    
        # sort each level by row
        # if row is the same, sort by value instead
        def compare(a, b):
            a_val, a_row = a
            b_val, b_row = b
            
            if a_row == b_row:
                return a_val - b_val
            else:
                return a_row - b_row
            
        for k in levels.keys():
            levels[k] = sorted(levels[k], key=cmp_to_key(compare))       

        # extract the node value into our results
        res = []
        for level in sorted(levels.keys()):
            res.append([p[0] for p in levels[level]])
        return res
