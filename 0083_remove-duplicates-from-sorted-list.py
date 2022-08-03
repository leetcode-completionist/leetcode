# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:     
        dummy = ListNode(val=None)

        # moving pointer to the end of the deduplicated list
        dedup = dummy

        node = head
        while node:
            if dedup.val != node.val:
                # not duplicate, include new value
                dedup.next = node
                dedup = dedup.next
                node = node.next
            else:
                # duplicate, skip
                node = node.next
                dedup.next = None
        
        return dummy.next
