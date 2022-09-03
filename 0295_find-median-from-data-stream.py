# https://leetcode.com/problems/find-median-from-data-stream/
import heapq

class MedianFinder:

    def __init__(self):
        self.left_half = [] # max_heap
        self.right_half = [] # min_heap

    def addNum(self, num: int) -> None:
        # push it onto the right_half first
        heapq.heappush(self.right_half, (num, num))
        
        # get a num back out from right_half
        # (it might be the same as before and that is okay)
        rank, num = heapq.heappop(self.right_half)
        
        # push it onto the left_half next
        heapq.heappush(self.left_half, (-rank, num))
        
        if len(self.left_half) > len(self.right_half):
            # our implementation only allows right_half to be greater
            rank, num = heapq.heappop(self.left_half)
            heapq.heappush(self.right_half, (-rank, num))
            

    def findMedian(self) -> float:
        if len(self.left_half) == len(self.right_half):
            _, left = self.left_half[0]
            _, right = self.right_half[0]

            return (left + right) / 2
        else:
            return self.right_half[0][-1]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
