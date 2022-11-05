# https://leetcode.com/problems/where-will-the-ball-fall/
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        balls = [i for i in range(n)]
        
        for row in grid:
            for i in range(n):
                ball_col = balls[i]
                if ball_col == -1:
                    # ball is stuck, ignore
                    continue
                if row[ball_col] == 1:
                    # ball will go right
                    if ball_col == n - 1:
                        # can't go right any further
                        balls[i] = -1
                    elif row[ball_col + 1] == 1:
                        # \ \
                        balls[i] += 1
                    else:
                        # v shaped
                        balls[i] = -1
                else:
                    # ball will go left
                    if ball_col == 0:
                        # can't go left any further
                        balls[i] = -1
                    elif row[ball_col - 1] == -1:
                        # / /
                        balls[i] -= 1
                    else:
                        # v shaped
                        balls[i] = -1

        return balls
