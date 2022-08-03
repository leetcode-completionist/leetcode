class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # everything to the left of p are unique
        p = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[p]:
                p += 1
                nums[p] = nums[i]
                count = 1
            elif count < 2:
                p += 1
                nums[p] = nums[i]
                count += 1

        # add 1 because p is zero-based index
        return p + 1
