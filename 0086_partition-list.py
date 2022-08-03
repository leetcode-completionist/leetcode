# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # create a dummy node for list of nodes less than x
        dummy_small = ListNode(val=None)
        
        # create a dummy node for list of nodes greater than or equal
        # to x
        dummy_large = ListNode(val=None)
        
        # running pointers
        small = dummy_small
        large = dummy_large
        
        node = head
        while node:
            if node.val < x:
                small.next = node
                node = node.next
                small = small.next
                small.next = None
            else:
                large.next = node
                node = node.next
                large = large.next
                large.next = None
        
        # link all large nodes to be after the last small node
        small.next = dummy_large.next
        
        # first small node is the new "head"
        return dummy_small.next
        
