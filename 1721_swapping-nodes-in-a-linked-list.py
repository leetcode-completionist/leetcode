# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = {}
        
        i = 1
        prev = None
        node = head
        while node:
            # store node with its previous node
            nodes[i] = node
            prev, node = node, node.next
            i += 1

        nodes[k].val, nodes[i - k].val = nodes[i - k].val, nodes[k].val
        
        return head
