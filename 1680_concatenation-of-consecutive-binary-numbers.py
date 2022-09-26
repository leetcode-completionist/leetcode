# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        b = ""
        for i in range(1, n + 1):
            b += "{0:b}".format(i)
        return int(b, 2) % (10 ** 9 + 7)
