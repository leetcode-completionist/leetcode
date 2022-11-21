# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        
        visited = set([tuple(entrance)])
        m, n = len(maze), len(maze[0])
        
        q = deque([
            tuple([entrance[0] + 1, entrance[1]]),
            tuple([entrance[0] - 1, entrance[1]]),
            tuple([entrance[0], entrance[1] + 1]),
            tuple([entrance[0], entrance[1] - 1]),
        ])
        
        res = 1
        while q:
            q_len = len(q)
            for _ in range(q_len):
                (i, j) = q.popleft()
                
                if (i < 0 or i == m or
                    j < 0 or j == n):
                    continue
                
                if (i, j) in visited:
                    continue
                
                visited.add((i, j))
                
                if maze[i][j] == "+":
                    continue
                
                if (i == 0 or i == m - 1 or
                    j == 0 or j == n - 1):
                    return res
                
                q.extend([
                    tuple([i + 1, j]),
                    tuple([i - 1, j]),
                    tuple([i, j + 1]),
                    tuple([i, j - 1]),
                ])
            res += 1
        
        return -1
