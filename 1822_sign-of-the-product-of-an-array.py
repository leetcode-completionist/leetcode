# https://leetcode.com/problems/sign-of-the-product-of-an-array/
from functools import reduce

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = reduce(lambda a, b: a * b, nums)
        
        if product == 0:
            return 0
        elif product > 0:
            return 1
        else:
            return -1
