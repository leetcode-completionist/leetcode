# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # Find target and connect all nodes to their parent node
        target = None
        nodes = [(root, None)]
        while nodes:
            node, parent = nodes.pop()
            if node.val == start:
                target = node                
            
            node.parent = parent
            if node.left:
                nodes.append((node.left, node))
            if node.right:
                nodes.append((node.right, node))

        # BFS until all we visit all nodes        
        res = -1
        
        q = deque([target])
        seen = set()
        while q:
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
                    
            res += 1
            
        return res
