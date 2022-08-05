# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=float("-inf"), next=head)
        node = head
        while node:
            tmp_next = node.next
            node.next = None
                        
            insert = dummy
            while insert.next and insert.next.val < node.val:
                insert = insert.next
            
            if insert.next != node:
                node.next = insert.next
                insert.next = node
            
            node = tmp_next
        
        return dummy.next
