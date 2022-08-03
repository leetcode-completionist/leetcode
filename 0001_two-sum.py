class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            match = target - num
            if match in seen:
                return [seen[match], i]
            seen[num] = i

        return []
