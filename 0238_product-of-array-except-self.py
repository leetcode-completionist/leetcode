# https://leetcode.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # initialize product array from left with first element
        left = [nums[0]] + [0] * (n - 1)
        
        # initialize product array from right with last element
        right = [0] * (n - 1) + [nums[-1]]
        
        # fill out product arrays
        for i in range(1, n):
            # mult everything from left to right
            left[i] = left[i - 1] * nums[i]
            
            # mult everything from right to left
            right[n - i - 1] = right[n - i] * nums[n - i - 1]
        
        res = []
        
        for i in range(len(left)):
            if i == 0:
                # no products to the left
                # use only products to the right
                res.append(right[i + 1])
            elif i == len(left) - 1:
                # no products to the right
                # use only products to the left
                res.append(left[i - 1])
            else:
                res.append(left[i - 1] * right[i + 1])
            
        return res
