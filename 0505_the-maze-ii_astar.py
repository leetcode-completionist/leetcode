# https://leetcode.com/problems/the-maze-ii/
import heapq

class Solution:
    
    def distance(self, a: Tuple[int], b: Tuple[int]) -> int:
        """
        Returns the distance it takes to travel from point 'a' to 'b'.
        
        Since we can only go up/down/left/right, we will use the
        Manhattan distance as our A* search heuristic.
        """
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:        
        m, n = len(maze), len(maze[0])
        
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        start, dest = tuple(start), tuple(destination)
        
        visited = set()
        
        heap = [(self.distance(start, dest), 0, start)]
        
        while heap:
            _, dist, coordinate = heapq.heappop(heap)
            
            if coordinate == dest:
                return dist
            
            if coordinate in visited:
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

                next_dist = new_dist + dist
                    
                # add a heuristic (i.e. how far we are from the
                # destination) to heap ordering. This is a composite
                # score of dist to dest and next_dist.
                heuristic = self.distance((i, j), dest) + next_dist
                    
                heapq.heappush(heap, (heuristic, new_dist + dist, (i, j)))
        
        # we weren't able to reach our destination
        return -1
