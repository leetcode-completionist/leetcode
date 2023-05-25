class Solution:
    
    DIRECTIONS = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        
        i, j = click
        if board[i][j] == "M":
            board[i][j] = "X"
            return board
        
        for row in board:
            print(row)
        
        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            
            if board[i][j] == "M":
                # bomb, stop
                return
            
            if board[i][j] == "B":
                # already revealed, stop
                return
            
            if board[i][j].isdigit():
                # already revealed, stop
                return
            
            digit = 0
            for d_i, d_j in Solution.DIRECTIONS:
                n_i, n_j = i + d_i, j + d_j
                if n_i < 0 or n_i >= m or n_j < 0 or n_j >= n:
                    continue
                if board[n_i][n_j] == "M":
                    digit += 1
            
            if digit == 0:
                board[i][j] = "B"
                
                for d_i, d_j in Solution.DIRECTIONS:
                    dfs(i + d_i, j + d_j)
                
            else:
                board[i][j] = str(digit)
            

            
        dfs(i, j)
        return board
                
