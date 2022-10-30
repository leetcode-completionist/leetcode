# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # if we have sufficient quotas to eliminate
        # the obstacles in the worst case, then the
        # shortest distance is the Manhattan distance.
        if k >= m + n - 2:
            return m + n - 2
        
        initial = (0, 0, k)
        
        visited = set([initial])
        
        q = deque([(initial, 0)])
        
        while q:
            q_len = len(q)
            for _ in range(q_len):
                (i, j, remaining), dist = q.popleft()
                
                if (i,  j) == (m - 1, n - 1):
                    return dist
                
                for i_change, j_change in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_i = i + i_change
                    new_j = j + j_change
                    if new_i < 0 or new_i == m or new_j < 0 or new_j == n:
                        # out of bounds
                        continue
                        
                    new_remaining = remaining - grid[new_i][new_j]
                    if new_remaining < 0:
                        # we can't remove any more obstacles
                        continue
                    
                    next_state = (new_i, new_j, new_remaining)
                    if next_state in visited:
                        # already visited
                        continue
                        
                    visited.add(next_state)
                    q.append((next_state, dist + 1))
        
        return -1
