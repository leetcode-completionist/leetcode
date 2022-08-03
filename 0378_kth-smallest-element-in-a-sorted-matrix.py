import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
                
        seen = set()
        heap = [(matrix[0][0],  (0, 0))]
        
        while heap:
            element,  (i, j) = heapq.heappop(heap)
            if k == 1:
                return element
            k -= 1
            
            # look to the right
            if i < n - 1 and (i + 1, j) not in seen:
                seen.add((i + 1, j))
                heapq.heappush(heap, (matrix[i + 1][j],  (i + 1, j)))

            # look to the bottom
            if j < m - 1 and (i, j + 1) not in seen:
                seen.add((i, j + 1))
                heapq.heappush(heap, (matrix[i][j + 1],  (i, j + 1)))
        
        raise Exception("Illegal state")
