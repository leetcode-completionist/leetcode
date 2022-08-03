# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        node = None
        
        while list1 or list2:
            if not list2 or (list1 and list1.val < list2.val):
                n_node = list1
                list1 = list1.next
                n_node.next = None
            else:
                n_node = list2
                list2 = list2.next
                n_node.next = None
                
            if not head:
                head = n_node
                node = n_node
            else:
                node.next = n_node
                node = node.next
                
        if list1:
            node.next = list1
        elif list2:
            node.next = list2
        
        return head
                
            
            
                
                
