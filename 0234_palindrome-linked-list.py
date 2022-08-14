# https://leetcode.com/problems/palindrome-linked-list/
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def getLength(self, node: ListNode) -> int:
        n = 0
        while node:
            n += 1
            node = node.next
        return n
    
    
    def reverse(self, node: ListNode) -> ListNode:
        start = None
        while node:
            tmp = node.next
            node.next = start
            start = node
            node = tmp
        return start

        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # find the total list length
        n = self.getLength(head)
        
        mid = n // 2
        
        # jump to the middle node
        # and keep track of the end of the left half
        i = mid
        left_end = None
        node = head
        while i:
            left_end = node
            node = node.next
            i -= 1
        
        # break left half away
        left_end.next = None
        
        if n % 2 == 1:
            # list is odd, so we can discard the middle element
            tmp = node.next
            node.next = None
            node = tmp
        
        # reverse the right half
        right_start = self.reverse(node)
        
        # iterate through both left and right halves
        l, r = head, right_start
        while l and r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        
        return True
