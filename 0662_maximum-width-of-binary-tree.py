# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        if not root:
            return res
        
        q = deque([(root, 0)])
        
        while q:
            left_bound = math.inf
            right_bound = -math.inf
            
            n = len(q)
            for _ in range(n):
                node, idx = q.popleft()
                
                # update bounds seen on this level
                left_bound = min(left_bound, idx)
                right_bound = max(right_bound, idx)
                
                if node.left:
                    q.append((node.left, idx * 2 + 1))
                if node.right:
                    q.append((node.right, idx * 2 + 2))
                
            res = max(res, right_bound - left_bound + 1)
        
        return res
