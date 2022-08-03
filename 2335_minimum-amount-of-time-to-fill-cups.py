import heapq

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        heap = [(-a, i) for i, a in enumerate(amount)]
        heapq.heapify(heap)
        
        res = 0
        while heap:
            if heap[0][0] == 0:
                heapq.heappop(heap)
                continue
            
            cup1 = heapq.heappop(heap)
            if not heap:
                res += -cup1[0]
                return res
            
            cup2 = heapq.heappop(heap)
            
            seconds = min(-cup1[0], -cup2[0])
            if heap:
                if -heap[0][0] == seconds:
                    seconds = 1
                else:
                    # greedily pour as many seconds as possible
                    # until the min is at cup3 amount
                    seconds -= -heap[0][0]
                            
            if cup1[0] + seconds < 0:
                heapq.heappush(heap, (cup1[0] + seconds, cup1[1]))
            if cup2[0] + seconds < 0:
                heapq.heappush(heap, (cup2[0] + seconds, cup2[1]))
            res += seconds
        
        return res
