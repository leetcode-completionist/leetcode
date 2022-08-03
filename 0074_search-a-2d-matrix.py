class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_col = [matrix[i][0] for i in range(len(matrix))]
        
        row_idx = self.search(first_col, target)
        col_idx = self.search(matrix[row_idx], target)
        
        return matrix[row_idx][col_idx] == target
        
        
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return r
