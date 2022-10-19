# https://leetcode.com/problems/wiggle-sort-ii/
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = sorted(nums)
        
        n = len(nums)
        mid = n // 2 + (n % 2 != 0)
        left = arr[:mid]
        right = arr[mid:]
        
        for i in range(0, n, 2):
            nums[i] = left.pop()
        for i in range(1, n, 2):
            nums[i] = right.pop()
