# https://leetcode.com/problems/middle-of-the-linked-list/
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
                
        return slow
