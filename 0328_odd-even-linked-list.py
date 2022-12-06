# https://leetcode.com/problems/odd-even-linked-list/submissions/
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        oddList = nextOdd = ListNode()
        evenList = nextEven = ListNode()
        
        i = 0
        node = head
        while node:
            if i % 2 == 0:
                # odd
                nextOdd.next = node
                node = node.next
                nextOdd = nextOdd.next
                nextOdd.next = None
            else:
                nextEven.next = node
                node = node.next
                nextEven = nextEven.next
                nextEven.next = None
            i += 1
            
        res = oddList.next
        nextOdd.next = evenList.next
        return res
