class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n < 3:
            # 0 step has 0 ways ()
            # 1 step has 1 way (1)
            # 2 steps have 2 ways (1+1), (2+0)
            return n
        # current step can be reached by
        # sum of ways from 1 OR 2 steps ahead
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
