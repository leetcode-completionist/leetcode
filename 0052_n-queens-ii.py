class Solution:
    def totalNQueens(self, n: int) -> int:
        seen_col = set()
        seen_left_diag = set()
        seen_right_diag = set()

        res = 0
        board = [["."] * n for i in range(n)]

        def solve(row: int) -> None:
            nonlocal res
            
            if row == n:
                # we reached the end successfully
                res += 1
                return
            
            for col in range(n):
                if col in seen_col:
                    continue
                
                # Push queen as far up and left diagonally
                # use the starting position of the diagonal
                # as identifier
                a = min(row, col)
                if (row - a, col - a) in seen_left_diag:
                    continue
                    
                # Push the queen as far down and left diagonally
                # use the starting position of the diagonal
                # as identifier
                b = min(n - row, col)
                if (row + b, col - b) in seen_right_diag:
                    continue
                    
                board[row][col] = "Q"
                seen_col.add(col)
                seen_left_diag.add((row - a, col - a))
                seen_right_diag.add((row + b, col - b))
                                
                solve(row + 1)
                
                # backtrack
                seen_col.remove(col)
                seen_left_diag.remove((row - a, col - a))
                seen_right_diag.remove((row + b, col - b))
                board[row][col] = "."
                
        solve(0)

        return res
