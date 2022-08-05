# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        This is a constant memory variation of the solution,
        using in-place merge sort O(nlog(n)):
        
        1. Start with k = 0

        2. Set a window of size 2 x (2^k), we can completely detach the nodes from
           the original list for easier reasoning

        3. Inside the window, traverse to (2^k)th node (this is the mid of the window)
           (2^k)th node will be the start of the second half of the window

        4. Initialize a pointer to "start" and another pointer to "mid": (2^k)th node and
            an "end". Use these nodes to detach nodes from the main list
        
        5. Mergesort the two halfs into one sorted window and relink it back into
           the original list.
        
        6. Repeat #2 - 5 for nodes in groups of (2*2^k)
        
        7. Increase k by 1 and repeat #2 - 6 until (2*2^k) is greater than the next power of 2
           greater than total number of nodes
        
        Note:
        
        k = 0, 2*2^k == window size of 2, 2^k == 1 is the start of second half

            [-1,5,3,4,0]
            [-1,5]
                 [3,4]
                     [0]
        
        k = 1, 2*2^k == window size of 4, 2^k == 2 is the start of second half
        
        
            [-1,5,3,4,0]
            [-1,3,4,5]
                     [0]
        
        k = 2, 2*2^k == window size of 8, 2^k == 4 is the start of second half
        
            [-1,5,3,4,0]
            [-1,0,3,4,5]
        
        k = 3, 2*2^k == window size of 16.
        
        We stop because 16 is > 8 (the next power of 2 greater than
        total number of nodes)
        """
        # No need to sort
        if not head or not head.next: return head
        
        # Grab the total size of list - O(n)
        size = 0
        node = head
        while node:
            size += 1
            node = node.next

        # Figure out how many iterations of merging we are going to perform
        k, pow2 = 0, 1
        while pow2 < size:
            k += 1
            pow2 *= 2
        
        # Start merging
        dummy = ListNode(val=float("-inf"), next=head)

        for i in range(k):
            prev = dummy
            node = dummy.next
            while node:
                prev, node = self.mergeWindow(i, prev, node)

        return dummy.next
    
    
    def mergeWindow(self,
                    k: int,
                    prev: ListNode,
                    node: Optional[ListNode]) -> (ListNode, Optional[ListNode]):
        """
        We return a tuple:
        
        tuple[1] is the next node that we should resume traversal from. This could be
        null, which will allow the caller to break out. This could also be the start of
        a next window.
        
        tuple[0] is the preceding node of tuple[1]. It is returned so we can pass it in again
        on the next mergeWindow call. This allows us to quickly link one sorted window to the
        next without needing to retraverse the list.
        """
        # temporarily break off from the list
        prev.next = None
        
        # maintain three pointers (start, mid, end)
        #
        # we will use these pointers to create the following segments:
        #
        # nodes from start - mid (non inclusive)
        # nodes from mid - end (non inclusive)
        # nodes from end - remainder 
        start, mid = node, node
        for i in range(2**k - 1):
            if not mid:
                break
            mid = mid.next
        
        if not mid:
            # not enough elements to merge, we can return early
            # before that we need to relink prev back to node
            prev.next = node
            return (node, None)
        
        # Unlink [start, mid)
        n = mid.next
        mid.next = None
        mid = n
        
        # Find end of window
        end = mid
        for i in range(2**k - 1):
            if not end:
                break
            end = end.next

        # Unlink [mid, end)
        if end:
            n = end.next
            end.next = None
            end = n

        # sorted list will be linked from prev
        sorted_window = prev
        
        # now we perform regular mergesort on nodes [start,mid) and [mid, end)
        while start and mid:
            if start.val <= mid.val:
                tmp = start.next
                sorted_window.next = start
                prev = sorted_window
                sorted_window = sorted_window.next
                sorted_window.next = None
                start = tmp
            else:
                tmp = mid.next
                sorted_window.next = mid
                prev = sorted_window
                sorted_window = sorted_window.next
                sorted_window.next = None
                mid = tmp
        
        # if there are still elements remaining, we will link them to
        # the sorted_window.
        #
        # we also traverse all the way to the end so that the caller will
        # know we are at the end of the list
        if start:
            sorted_window.next = start
            while sorted_window:
                prev = sorted_window
                sorted_window = sorted_window.next
                
        if mid:
            sorted_window.next = mid
            while sorted_window:
                prev = sorted_window
                sorted_window = sorted_window.next
        
        prev.next = end
        return (prev, end)
