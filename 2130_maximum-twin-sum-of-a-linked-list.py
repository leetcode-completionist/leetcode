from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dq = deque()
        
        node = head
        while node:
            dq.append(node.val)
            node = node.next
            
        res = 0
        while dq:
            res = max(res, dq.popleft() + dq.pop())
        return res
