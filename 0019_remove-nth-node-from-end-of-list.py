# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Single pass with three pointers
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        # Pointer to Nth - 1 node
        ll = None
        # Pointer to Nth node
        l = None
        # Pointer to iterate through the list until the end
        r = head
        
        # Advance r for n elements
        while n:
            r = r.next
            n -= 1
        
        # Start advancing l starting at head
        l = head
        
        while r:
            ll = l
            l = l.next
            r = r.next
        
        # If Nth - 1 node is null, Nth + 1 node will be the new head
        if not ll:
            return l.next
        
        # Remove Nth node
        ll.next = l.next

        return head
        
