# https://leetcode.com/problems/game-of-life/
class Solution:
    
    ALIVE = set([-2, 1])
    
    DEAD = set([-1, 0])
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        Intermediary states:
        
        -1: dead cell (0) that will become alive (1)
        -2: alive cell (1) that will become dead (0)
        """
        
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                alive_neighbors = 0
                
                # top left
                if i - 1 >= 0 and j - 1 >= 0:
                    if board[i- 1][j - 1] in Solution.ALIVE:
                        alive_neighbors += 1
                
                # top
                if i - 1 >= 0:
                    if board[i - 1][j] in Solution.ALIVE:
                        alive_neighbors += 1
                        
                # top right
                if i - 1 >= 0 and j + 1 < n:
                    if board[i - 1][j + 1] in Solution.ALIVE:
                        alive_neighbors += 1
                        
                # left
                if j - 1 >= 0:
                    if board[i][j - 1] in Solution.ALIVE:
                        alive_neighbors += 1
                        
                # right
                if j + 1 < n:
                    if board[i][j + 1] in Solution.ALIVE:
                        alive_neighbors += 1
                        
                # bottom left
                if i + 1 < m and j - 1 >= 0:
                    if board[i + 1][j - 1] in Solution.ALIVE:
                        alive_neighbors += 1
                        
                # bottom
                if i + 1 < m:
                    if board[i + 1][j] in Solution.ALIVE:
                        alive_neighbors += 1
                        
                # bottom right
                if i + 1 < m and j + 1 < n:
                    if board[i + 1][j + 1] in Solution.ALIVE:
                        alive_neighbors += 1
                        
                if board[i][j] == 1:
                    # previously alive
                    if 2 <= alive_neighbors <= 3:
                        # remains alive
                        continue
                    else:
                        # else dead will be dead
                        board[i][j] = -2
                else:
                    # previously dead
                    if alive_neighbors == 3:
                        # reproduction
                        board[i][j] = -1
        
        # change intermediary values to their new state
        for i in range(m):
            for j in range(n):
                if board[i][j] == -2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1
