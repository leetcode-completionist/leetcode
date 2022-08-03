# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:   
        if not head:
          return None
        
        # store all nodes in a list first
        l = []
        node = head
        while node:
          l.append(node)
          node = node.next
        
        # reduce k by modding len(l)
        # since we know a full len(l) rotation is
        # equivalent to no rotation
        k = k % len(l)

        if len(l) < 2 or k == 0:
          # a single node or a k-value of zero
          # means no rotation
          return head
        
        # starting from the end of the list
        # rotate through the list
        pointer = len(l) - 1
        for i in range(k - 1):
          # we know pointer will never go negative
          # because we have modded it before
          pointer -= 1
        
        # if pointer is at the front of the list
        # return list as-is
        if pointer == 0:
          return l[pointer]
        
        # make the previous node the end
        l[pointer - 1].next = None
        
        # link up remainder of the list to head
        l[-1].next = head
        
        # our pointer points to the head of the new list
        return l[pointer]
