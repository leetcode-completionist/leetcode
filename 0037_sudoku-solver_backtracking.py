class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        seen_row = set()
        seen_col = set()
        seen_square = set()

        # add immutable cells to seen first
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != ".":
                    seen_row.add((j, c))
                    seen_col.add((i, c))
                    seen_square.add((i // 3, j // 3, c))

        def solve() -> None:
            for i in range(9):
                for j in range(9):
                    c = board[i][j]
                    if c != ".":
                        continue
                        
                    # a new empty cell, try all options (e.g. 1 ... 9)
                    for k in range(1, 10):
                        option = str(k)
                        
                        # check if option is eligible
                        if (j, option) in seen_row:
                            continue
                        if (i, option) in seen_col:
                            continue
                        if (i // 3, j // 3, option) in seen_square:
                            continue

                        # eligible option
                        board[i][j] = option

                        # add to seen
                        seen_row.add((j, option))
                        seen_col.add((i, option))
                        seen_square.add((i // 3, j // 3, option))

                        # fill out the rest of the board if possible
                        if solve():
                            return True

                        # option is invalid, backtrack
                        seen_row.remove((j, option))
                        seen_col.remove((i, option))
                        seen_square.remove((i // 3, j // 3, option))
                        board[i][j] = "."

                    # we have exhausted all options at this cell
                    return False
            
            # end of the board, we have a valid solution
            return True

        # iterate through all cells and fill out empty cells
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == "." and solve():
                    return
