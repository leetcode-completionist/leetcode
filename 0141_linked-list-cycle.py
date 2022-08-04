# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow, fast = head, head.next
        
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
        
        while slow != fast:
            if not fast or not fast.next:
                return False

            slow = slow.next
            fast = fast.next.next
            
        return True
