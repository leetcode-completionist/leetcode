# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root: TreeNode) -> str:
        """
        Encodes a tree to a single string.
        """        
        if not root:
            return ""
        
        arr = []
        
        # fill up an array via BFS (including null values)
        # so parent/children are in the proper locations
        q = deque([root])
        
        # we stop BFS as soon as we do not encounter any further
        # values
        has_node = True
        while q and has_node:
            has_node = False
            
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node == None:
                    arr.append(None)
                else:
                    arr.append(node.val)
                    has_node = True
                    q.append(node.left)
                    q.append(node.right)
        
        # trim trailing nulls
        while arr[-1] == None:
            arr.pop()
            
        return ",".join([str(val) if val != None else "null" for val in arr])
        

    def deserialize(self, data: str) -> TreeNode:
        """
        Decodes your encoded data to tree.
        """
        if not data:
            return None
        
        tokens = data.split(",")
        
        # initialize nodes
        nodes = map(
            lambda token: TreeNode(token) if token != None else None,
            tokens,
        )
        nodes = list(nodes)
        
        n = len(nodes)
        
        # iterate through each node and set its left/right children
        for i in range(n):
            node = nodes[i]
            
            if node == None:
                continue
            
            left_child = i * 2 + 1
            if left_child < n:
                node.left = nodes[left_child]
            
            right_child = i * 2 + 2
            if right_child < n:
                node.right = nodes[right_child]

        return nodes[0]

    
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
