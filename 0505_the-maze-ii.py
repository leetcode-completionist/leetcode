# https://leetcode.com/problems/the-maze-ii/
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        visited = {}
        
        q = deque([(start[0], start[1], 0)])
        
        while q:
            q_len = len(q)
            for _ in range(q_len):
                row, col, dist = q.popleft()
                        
                if (row, col) in visited and visited[(row, col)] <= dist:
                    # we can reach this location with lower
                    # distance count
                    continue
                
                visited[(row, col)] = dist
                
                # go all four directions
                for direction in directions:
                    i, j = row, col
                    new_dist = 0
                    
                    # keep going until we hit a wall
                    while (0 <= i + direction[0] < m and
                           0 <= j + direction[1] < n and
                           maze[i + direction[0]][j + direction[1]] == 0):
                        i += direction[0]
                        j += direction[1]
                        new_dist += 1
                    
                    q.append((i, j, new_dist + dist))
                
        dest = tuple(destination)
        
        if dest in visited:
            return visited[dest]
        else:
            return -1
