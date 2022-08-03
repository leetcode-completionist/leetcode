class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        
        is_negative = n < 0
        n = abs(n)

        m = n // 2

        res = self.myPow(x, m)
        res *= res
        if n % 2 == 1:
            res *= x

        if is_negative:
            return 1/res
        return res
