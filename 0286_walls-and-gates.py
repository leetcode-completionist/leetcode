# https://leetcode.com/problems/walls-and-gates/
class Solution:
    
    INF = 2**31 - 1
    
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        
        q = deque()
        
        # find all gates and make the first move
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i + 1, j, 1))
                    q.append((i - 1, j, 1))
                    q.append((i, j + 1, 1))
                    q.append((i, j - 1, 1))
                    
        
        while q:
            q_len = len(q)
            for _ in range(q_len):
                i, j, dist = q.popleft()
                
                if i < 0 or i == m or j < 0 or j == n:
                    # out of bounds
                    continue
                    
                if rooms[i][j] != Solution.INF:
                    # not an empty room
                    continue
                    
                rooms[i][j] = dist
                
                q.append((i + 1, j, dist + 1))
                q.append((i - 1, j, dist + 1))
                q.append((i, j + 1, dist + 1))
                q.append((i, j - 1, dist + 1))
