class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_col = set()
        seen_row = set()
        seen_square = set()
        
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == ".":
                    continue
                
                if (j, c) in seen_col:
                    return False
                if (i, c) in seen_row:
                    return False
                if (i // 3, j // 3, c) in seen_square:
                    return False
                
                seen_col.add((j, c))
                seen_row.add((i, c))
                seen_square.add((i // 3, j // 3, c))
        
        return True
