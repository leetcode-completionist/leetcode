# https://leetcode.com/problems/01-matrix/
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        res = [[math.inf] * n for _ in range(m)]
        
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j, 0))

        while q:
            q_len = len(q)
            for _ in range(q_len):
                i, j, dist = q.popleft()

                if i < 0 or i == m or j < 0 or j == n:
                    continue

                dist = 0 if mat[i][j] == 0 else dist + 1

                if res[i][j] <= dist:
                    continue

                res[i][j] = dist

                q.append((i + 1, j, dist))
                q.append((i - 1, j, dist))
                q.append((i, j + 1, dist))
                q.append((i, j - 1, dist))

        return res
