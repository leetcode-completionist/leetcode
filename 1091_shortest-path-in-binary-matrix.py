from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:        
        m, n = len(grid), len(grid[0])
        
        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            # impossible
            return -1
        
        visited = {}
        
        q = deque([((0, 0), 1)])
        
        while q:
            q_len = len(q)
            for _ in range(q_len):
                coord, d = q.popleft()
            
                if coord == (m - 1, n - 1):
                    return d
            
                if coord in visited and visited[coord] <= d:
                    # already visited with shorter distance
                    continue
                    
                visited[coord] = d
                
                for d_i, d_j in [
                  (-1, -1),
                  (-1, 0),
                  (-1, 1),
                  (0, -1),
                  (0, 1),
                  (1, -1),
                  (1, 0),
                  (1, 1),
                ]:
                    new_i, new_j = coord[0] + d_i, coord[1] + d_j
                    if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                        continue
                    if grid[new_i][new_j] == 1:
                        continue
                    q.append(((new_i, new_j), d + 1))
                    
        return -1
        
