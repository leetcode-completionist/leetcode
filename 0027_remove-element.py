class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = -1
        
        for i in range(len(nums)):
            if nums[i] != val:
                res += 1
                nums[res] = nums[i]

        return res + 1
