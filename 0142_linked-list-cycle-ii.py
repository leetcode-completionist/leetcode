# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        intersection = self.getCycle(head)
        if not intersection:
            return None
        
        p1, p2 = head, intersection
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1
    
    
    def getCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Uses Floyd's Tortoise and Hare algorithm to detect cycles and
        return the node where a cycle was originally detected.
        
        Note, this node is NOT NECESSARILY where the cycle BEGINS.
        """        
        # fast pointer travels in 2 steps
        # slow pointer travers in 1 step
        #
        # if there are no cycles, fast pointer will get to null first
        # if there is a cycle, fast pointer will eventually catch up to
        # slow pointer.
        #
        # we can be sure that fast will always reach slow.
        # if slow moves by one and fast moves by two, then fast is
        # closing in on slow by 1 space each iteration.
        #
        # eventually the distance between the two will be zero, and thus
        # a cycle has been detected.
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
            if slow == fast:
                return slow

        return None
