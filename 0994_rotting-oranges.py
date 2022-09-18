# https://leetcode.com/problems/rotting-oranges/
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        fresh_oranges = set()
        
        rotten_oranges = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_oranges.add((i, j))
                elif grid[i][j] == 2:
                    rotten_oranges.append((i, j))
                    
        minutes = 0
        while rotten_oranges:
            count = len(rotten_oranges)
            for _ in range(count):
                rotten_i, rotten_j = rotten_oranges.popleft()
                
                for delta_i, delta_j in [(1,0), (-1,0), (0,1), (0,-1)]:
                    orange = (rotten_i + delta_i, rotten_j + delta_j)
                    if orange in fresh_oranges:
                        fresh_oranges.remove(orange)
                        rotten_oranges.append(orange)
            
            if rotten_oranges:
                minutes += 1
        
        return minutes if not fresh_oranges else -1
