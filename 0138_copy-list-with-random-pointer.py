"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_to_clone = {}
        
        def copy(node: 'Optional[Node]') -> 'Optional[Node]':
            if not node:
                return None
            
            if node in original_to_clone:
                return original_to_clone[node]
                       
            clone = Node(node.val)
            original_to_clone[node] = clone
            
            if node.next:
                clone.next = copy(node.next)
            if node.random:
                clone.random = copy(node.random)
                
            return clone
        
        return copy(head)
