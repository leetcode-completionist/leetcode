# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        left = 0
        
        minK_index = -1
        maxK_index = -1
        
        res = 0

        for right, num in enumerate(nums):
            if num < minK or num > maxK:
                left = right + 1
                continue

            if num == minK:
                minK_index = right
            if num == maxK:
                maxK_index = right

            if minK_index >= left and maxK_index >= left:
                res += min(minK_index, maxK_index) - left + 1

        return res
