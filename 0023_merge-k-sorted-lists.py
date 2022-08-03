import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # push first node of each list into the heap
        for i, l in enumerate(lists):
            if not l:
                # input could contain null nodes
                continue
            # we use i as tie-breaker when storing tuples
            heapq.heappush(heap, (l.val, i, l))
        
        head = node = ListNode()
        while heap:
            _, i, l = heapq.heappop(heap)

            if l.next:
                # push next node back onto the heap
                # we can reuse the i as tie-breaker
                heapq.heappush(heap, (l.next.val, i, l.next))
            
            node.next = l
            l.next = None
            node = node.next
        
        return head.next
