# https://leetcode.com/problems/the-maze-ii/
import heapq

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:        
        m, n = len(maze), len(maze[0])
        
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        start, destination = tuple(start), tuple(destination)
        
        visited = set()
        
        heap = [(0, start)]
        
        while heap:
            dist, coordinate = heapq.heappop(heap)
            
            if coordinate == destination:
                # we reached our destination, return the distance
                # directly since Dijkstra's algorithm guarantees
                # nodes appearing in shortest distance ordering.
                return dist
            
            if coordinate in visited:
                # we've previously reached this location
                # with Dijkstra's, it is guaranteed that we
                # found a shorter distance to the location previously
                continue
            
            visited.add(coordinate)

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

                heapq.heappush(heap, (new_dist + dist, (i, j)))
        
        # we weren't able to reach our destination
        return -1
