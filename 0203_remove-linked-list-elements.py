# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(val=math.inf, next=head)
        prev = dummy
        node = head
        while node:
            if node.val == val:
                # unlink current node
                prev.next = node.next
                # note we DO NOT update
                # prev
            else:
                # we update prev
                prev = node
            # we always move onto the next node
            node = node.next
        return dummy.next
