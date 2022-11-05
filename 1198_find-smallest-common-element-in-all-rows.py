# https://leetcode.com/problems/find-smallest-common-element-in-all-rows/
class Solution:
    def binSearch(nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:            
            m = l + (r - l) // 2
            mid = nums[m]
            if mid < target:
                l = m + 1
            elif mid > target:
                r = m - 1
            else:
                return m
        return -1
    
    
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        for candidate in mat[0]:
            # for each num in the first row
            common = True
            for row in mat[1:]:
                # see if num is common to all rows
                idx = Solution.binSearch(row, candidate)
                if idx == -1:
                    common = False
                    break
            if common:
                return candidate

        # no smallest common elemenbt
        return -1
