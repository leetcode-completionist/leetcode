# https://leetcode.com/problems/shortest-distance-from-all-buildings/
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        distances = [[0] * n for _ in range(m)]

        houses = []
        empty = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    empty.add((i, j))
                elif grid[i][j] == 1:
                    houses.append((i, j))

        def bfs(start_i, start_j) -> None:
            visited = set()
            q = deque([
                (start_i + 1, start_j, 1),
                (start_i - 1, start_j, 1),
                (start_i, start_j + 1, 1),
                (start_i, start_j - 1, 1),
            ])
            while q:
                q_len = len(q)
                for _ in range(q_len):
                    i, j, dist = q.popleft()
                    if (i < 0 or i == m or
                        j < 0 or j == n or
                        (i, j) in visited or
                        (i, j) not in empty):
                        continue
                    
                    visited.add((i, j))
                    distances[i][j] += dist

                    dist += 1
                    q.append((i + 1, j, dist))
                    q.append((i - 1, j, dist))
                    q.append((i, j + 1, dist))
                    q.append((i, j - 1, dist))

            # optimization to address TLEs
            unreachable = empty - visited
            for i, j in unreachable:
                grid[i][j] = -1
                empty.remove((i, j))

        for i, j in houses:
            bfs(i, j)

        res = math.inf
        for i, j in empty:
            res = min(res, distances[i][j])

        return -1 if res == math.inf else res
