# https://leetcode.com/problems/delete-node-in-a-linked-list/
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # shift all subsequent values forward by one
        prev = None
        while node.next:
            node.val = node.next.val
            prev = node
            node = node.next
        
        # then delete the last node
        prev.next = None
