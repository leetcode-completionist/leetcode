class Solution:

    VISITED = "."

    def solve(self, matrix: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i == m or j == n:
                return
            
            if matrix[i][j] == "X" or matrix[i][j] == Solution.VISITED:
                return
            
            matrix[i][j] = Solution.VISITED
            
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)
        
        
        for i in range(n):
            if matrix[0][i] == "O":
                dfs(0, i)
            if matrix[m - 1][i] == "O":
                dfs(m - 1, i)
        for i in range(m):
            if matrix[i][0] == "O":
                dfs(i, 0)
            if matrix[i][n - 1] == "O":
                dfs(i, n - 1)
                
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == Solution.VISITED:
                    matrix[i][j] = "O"
                elif matrix[i][j] == "O":
                    matrix[i][j] = "X"
