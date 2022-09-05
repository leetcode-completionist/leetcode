# https://leetcode.com/problems/game-of-life/
class Solution:
    
    ALIVE = set([-2, 1])
    
    DEAD = set([-1, 0])
    
    DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
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
                
                # count alive neighbors
                for i_delta, j_delta in Solution.DIRS:
                    x, y = i + i_delta, j + j_delta
                    if x < 0 or x == m or y < 0 or y == n:
                        # out of bounds
                        continue

                    if board[x][y] in Solution.ALIVE:
                        alive_neighbors += 1
                        
                    if alive_neighbors > 3:
                        # already more than three
                        # no need to count further
                        break
                        
                if board[i][j] == 1:
                    # previously alive
                    if 2 <= alive_neighbors <= 3:
                        # remains alive
                        continue
                    else:
                        # else cell will be dead
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
                    
