# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode()
        
        # moving pointer to the end of the deduplicated list
        dedup = dummy

        seen, is_dup = head, False
        node = head.next
        seen.next = None
        while node:
            if not seen:
                seen = node
                node = node.next
                seen.next = None
            elif seen.val != node.val:
                # add seen to dedup list if not a dup
                if not is_dup:
                    dedup.next = seen
                    dedup = dedup.next
                
                # and make current node as seen
                seen = node
                node = node.next
                seen.next = None
                is_dup = False
            else:
                # current node same as seen, mark it as dup
                is_dup = True
                node = node.next
        
        if seen and not is_dup:
            dedup.next = seen
        
        return dummy.next
