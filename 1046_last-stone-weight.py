# https://leetcode.com/problems/last-stone-weight/
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        for stone in stones:
            heapq.heappush(heap, (-stone, stone))
        
        while len(heap) > 1:
            _, bigger = heapq.heappop(heap)
            _, smaller = heapq.heappop(heap)
            
            bigger -= smaller
            
            if bigger:
                heapq.heappush(heap, (-bigger, bigger))
            
        if not heap:
            return 0
        
        return heap[0][1]
