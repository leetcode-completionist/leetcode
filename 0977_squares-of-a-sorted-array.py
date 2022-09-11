# https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        
        l, r = 0, len(nums) - 1
        while l <= r:
            a = abs(nums[l])
            b = abs(nums[r])
            
            if a >= b:
                res.append(a ** 2)
                l += 1
            else:
                res.append(b ** 2)
                r -= 1
        
        res.reverse()
        return res
