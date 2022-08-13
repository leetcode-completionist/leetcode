class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = defaultdict(list)
        for i in range(len(nums)):
            if nums[i] in seen and i - seen[nums[i]][-1] <= k:
                return True
            seen[nums[i]].append(i)
        return False
