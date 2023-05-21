class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i: int, j: int):
            if i < 0 or i >= m or j < 0 or j >= n:
                # out of bounds
                return
            if grid[i][j] == -1:
                # already visited
                return
            if grid[i][j] == 0:
                # empty
                return
            grid[i][j] = -1
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            
        def labelFirstIsland():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        return dfs(i, j)    
            
        labelFirstIsland()
        
        # Grab a list of starting coords from other island
        # These coords must be next to the ocean.
        q = list()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i + 1 < m and grid[i + 1][j] == 0:
                        q.append((i + 1, j, 0))
                    if i - 1 > -1 and grid[i - 1][j] == 0:
                        q.append((i - 1, j, 0))
                    if j + 1 < n and grid[i][j + 1] == 0:
                        q.append((i, j + 1, 0))
                    if j - 1 > -1 and grid[i][j - 1] == 0:
                        q.append((i, j - 1, 0))

        # Perform BFS towards ocean until we reach other island                
        q = deque(q)
        while q:
            q_len = len(q)
            for _ in range(q_len):
                i, j, d = q.popleft()
                if i < 0 or i >= m or j < 0 or j >= n:
                    # out of bounds
                    continue                
                if grid[i][j] == 1:
                    # we need to go out towards island 1
                    continue
                if grid[i][j] == 2:
                    # we already traversed here
                    continue
                if grid[i][j] == -1:
                    # we reached the other island
                    return d
                # label as visited
                grid[i][j] = 2
                
                q.append((i + 1, j, d + 1))
                q.append((i - 1, j, d + 1))
                q.append((i, j + 1, d + 1))
                q.append((i, j - 1, d + 1))
        
        return -1
