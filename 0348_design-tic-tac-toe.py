class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[None] * n for _ in range(n)]

        
    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        
        if self.__check_vertical(player=player, col=col):
            return player
        
        if self.__check_horizontal(player=player, row=row):
            return player

        if row == col and self.__check_diag(player=player):
            return player

        if col == (self.n - row - 1) and self.__check_anti_diag(player=player):
            return player
        
        return 0        
        
            
    def __check_vertical(self, player: int, col: int) -> bool:
        for i in range(self.n):
            if self.board[i][col] != player:
                return False
        return True
    
    
    def __check_horizontal(self, player: int, row: int) -> bool:
        for j in range(self.n):
            if self.board[row][j] != player:
                return False
        return True
    
    
    def __check_diag(self, player: int) -> bool:
        i, j = 0, 0
        for x in range(self.n):
            if self.board[i + x][j + x] != player:
                return False
        return True
    
    
    def __check_anti_diag(self, player: int) -> bool:
        i, j = 0, self.n - 1
        for x in range(self.n):
            if self.board[i + x][j - x] != player:
                return False
        return True
    

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
