class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # everything to the left of zero_p will be 0
        zero_p = 0
        # everything to the right of two_p will be 2
        two_p = len(nums) - 1
        
        # iterate through each c
        i = 0
        while i <= two_p:
            # once we reach two_p, we can assume everything to
            # the right is already 2's
            if nums[i] == 0:
                # we swap with zero_p
                nums[zero_p], nums[i] = nums[i], nums[zero_p]
                # move zero_p to the right by 1
                zero_p += 1
                # we can move on to the next char
                i += 1
            elif nums[i] == 2:
                # we swap with two_p
                nums[two_p], nums[i] = nums[i], nums[two_p]
                # move two_p to the left by 1
                two_p -= 1
                # we might've swapped a 2 to nums[i]
                # with two_p updated, we will recheck nums[i]
                continue
            else:
                # nums[i] == 1 so we can do nothing and move on
                i += 1
