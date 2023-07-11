from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.parent = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Connect each node to its parent        
        nodes = [(root, None)]
        while nodes:
            node, parent = nodes.pop()
            node.parent = parent
            if node.left:
                nodes.append((node.left, node))
            if node.right:
                nodes.append((node.right, node))
            
        # BFS k steps away
        q = deque([target])
        seen = set()
        while q and k:
            k -= 1
            
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                seen.add(node)
                
                if node.left and node.left not in seen:
                    q.append(node.left)
                if node.right and node.right not in seen:
                    q.append(node.right)
                if node.parent and node.parent not in seen:
                    q.append(node.parent)
                    
        return [node.val for node in q]
