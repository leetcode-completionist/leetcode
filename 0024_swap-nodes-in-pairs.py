# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        prev = dummy
        node = head
        while node and node.next:
            next_node = node.next
            node.next = next_node.next
            next_node.next = node
            
            prev.next = next_node
            prev = node
            node = node.next
        
        return dummy.next
