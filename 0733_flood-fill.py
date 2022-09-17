# https://leetcode.com/problems/flood-fill/
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        
        def dfs(i: int, j: int, prev_color: int) -> None:
            if i < 0 or i == m or j < 0 or j == n:
                return
            
            if image[i][j] != prev_color:
                # not in the same flood zone
                return
            
            if image[i][j] == color:
                # already same color
                return
            
            prev_color = image[i][j]
            
            image[i][j] = color
            
            dfs(i + 1, j, prev_color)
            dfs(i - 1, j, prev_color)
            dfs(i, j + 1, prev_color)
            dfs(i, j - 1, prev_color)
            
        dfs(sr, sc, image[sr][sc])
        
        return image
