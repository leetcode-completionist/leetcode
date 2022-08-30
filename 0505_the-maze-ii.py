# https://leetcode.com/problems/the-maze-ii/
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        visited = {}
        
        start, destination = tuple(start), tuple(destination)
		
        q = deque([(0, start)])
        
        while q:
            q_len = len(q)
            for _ in range(q_len):
                dist, coordinate = q.popleft()
                        
                if coordinate in visited and visited[coordinate] <= dist:
                    # we can reach this location with lower
                    # distance count
                    continue
                
                visited[coordinate] = dist
                
                # go all four directions
                for direction in directions:
                    i, j = coordinate
                    new_dist = 0
                    
                    # keep going until we hit a wall
                    while (0 <= i + direction[0] < m and
                           0 <= j + direction[1] < n and
                           maze[i + direction[0]][j + direction[1]] == 0):
                        i += direction[0]
                        j += direction[1]
                        new_dist += 1
                    
                    q.append((new_dist + dist, (i, j)))
        
        if destination in visited:
            return visited[destination]
        else:
            return -1
