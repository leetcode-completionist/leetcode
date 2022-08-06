# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # find the length of list a (O(m))
        a_length = 0
        node = headA
        while node:
            a_length += 1
            node = node.next
            
        # find the length of list b (O(n))
        b_length = 0
        node = headB
        while node:
            b_length += 1
            node = node.next
            
        short, long = headA, headB
        if a_length > b_length:
            short, long = long, short
        
        # give long list a head start
        head_start = abs(a_length - b_length)
        while head_start and long:
            long = long.next
            head_start -= 1
            
        # iterate until we intersect
        while short and long:
            if short == long:
                return short
            
            short = short.next
            long = long.next
        
        # no intersection
        return None
