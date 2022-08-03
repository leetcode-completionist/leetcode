class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                # find next largest
                next_larger = i + 1
                for j in range(i + 1, len(nums)):
                    # if duplicate values, find the rightmost
                    if nums[j] > nums[i] and nums[j] <= nums[next_larger]:
                        next_larger = j
                nums[i], nums[next_larger] = nums[next_larger], nums[i]

                # reverse remaining elements
                nums[i + 1:] = nums[i + 1:][::-1]
                return
        
        # no next permutation, reverse entire list
        nums.reverse()
