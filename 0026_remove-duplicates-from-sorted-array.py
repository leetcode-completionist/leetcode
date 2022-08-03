class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        # keeps track of the last valid element
        res = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[res]:
                # duplicate, move on
                continue
            # not a duplicate, increase res by one
            res += 1
            # overwrite existing value with new number
            nums[res] = nums[i]
        
        # return the count by adding one to index
        # rest of the array is ignored
        return res + 1
