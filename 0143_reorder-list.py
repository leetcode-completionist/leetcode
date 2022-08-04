# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            # reordering only starts with list of 3 nodes or more
            return head
        
        # 1. Find the middle node
        #
        # Traverse the entire list to
        # count how many nodes we have
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        n = (n - 1) // 2

        # Traverse from head up to middle
        mid = head
        while n:
            mid = mid.next
            n -= 1
        
        # 2. Reverse sub-list starting at mid + 1
        node = mid.next
        mid.next = None
        
        reverse = None
        while node:
            tmp = node.next
            node.next = reverse
            reverse = node
            node = tmp
        
        # 3. Merge first half of list with reversed(second half)
        node = head
        while node:
            tmp = node.next
            
            # Weave a node in from reverse list
            if reverse:
                node.next = reverse
                reverse = reverse.next
                node = node.next
            
            # Weave back into first half of list
            node.next = tmp
            node = node.next
        
        return head
