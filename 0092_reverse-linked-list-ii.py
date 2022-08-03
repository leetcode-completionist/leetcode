# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            # no need to reverse if left and right are the same
            return head
        
        dummy = ListNode(val=None, next=head)

        i = 1   # running counter
        node = head
        prev = dummy
        while node:
            if i > right:
                # we went past right, so no further work is needed
                break
                
            if i < left:
                # we haven't reached the nodes we need to reverse yet
                prev = node
                node = node.next
                i += 1
                continue
            
            # we are inside left/right and will need to reverse the list
            tail = None
            r_list = None
            while i <= right and node:
                if not tail:
                    # keep track of first node as the tail
                    tail = node
                # reverse linked list in place
                tmp = node.next
                node.next = r_list
                r_list = node
                node = tmp
                i += 1
            
            # relink reversed list back to the input list
            prev.next = r_list
            prev = prev.next
            if tail:
                tail.next = node
        
        return dummy.next
