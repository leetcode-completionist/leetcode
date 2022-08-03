class Solution:

    VISITED = "."
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        # build requirements
        req = {}
        for c in word:
            if c not in req:
                req[c] = 0
            req[c] += 1

        # decide if we search for word from the left or right
        # we can reduce number of paths by choosing the side
        # with least freq
        if req[word[0]] > req[word[-1]]:
            word = word[::-1]
            
        # keep track of how many 'keys' in req we meet
        # i.e. decreasing the count till zero
        formed = 0
        for i in range(m):
            for j in range(n):
                if (c := board[i][j]) in req:
                    req[c] -= 1
                    if req[c] == 0:
                        formed += 1

        # validate if board contains enough letters to form word
        if formed < len(req.keys()):
            return False
        
        # at this point, we can start traversing the board via
        # regular dfs and return as soon as we have a match
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and self.dfs(board, i, j, word):
                    return True
        return False
                    
        
    def dfs(self, board: List[List[str]], i: int, j: int, word: str) -> bool:
        if not word:
            # we've matched every char in word
            return True

        if (i < 0 or i == len(board) or j < 0 or j == len(board[i]) or
            board[i][j] != word[0] or
            board[i][j] == Solution.VISITED):
            # impossible to build word from here
            return False

        # mark as visited to prevent infinite recursion
        before = board[i][j]
        board[i][j] = Solution.VISITED

        # match one char
        word = word[1:]

        # dfs all four directions
        res = (self.dfs(board, i - 1, j, word) or
               self.dfs(board, i + 1, j, word) or
               self.dfs(board, i, j - 1, word) or
               self.dfs(board, i, j + 1, word))

        # backtrack
        board[i][j] = before

        return res
