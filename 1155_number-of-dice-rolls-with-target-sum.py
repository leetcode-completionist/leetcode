# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
class Solution:
    def numRollsToTarget(self, dice: int, faces: int, target: int) -> int:
        dp = [[0 for _ in range(target+1)] for _ in range(dice)]

        # initialize DP with first die
        dp[0][0] = 0
        for i in range(1, min(faces, target) + 1):
            dp[0][i] = 1

        for z in range(1, dice):
            for i in range(1, target + 1):
                for x in range(1, faces + 1):
                    if i - x >= 0:
                        dp[z][i] += dp[z - 1][i - x]

        return dp[-1][-1] % 1000000007
