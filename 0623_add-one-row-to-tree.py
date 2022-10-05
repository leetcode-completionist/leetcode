# https://leetcode.com/problems/add-one-row-to-tree/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            # edge case
            return TreeNode(val=val, left=root)

        q = deque([(root, True, None)])
        for i in range(1, depth):
            n = len(q)
            for _ in range(n):
                node, _, _ = q.popleft()
                if not node:
                    continue
                q.append((node.left, True, node))
                q.append((node.right, False, node))
                    

        for node, is_left, parent in q:
            if is_left:
                parent.left = TreeNode(val=val, left=node)
            else:
                parent.right = TreeNode(val=val, right=node)

        return root
