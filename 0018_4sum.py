class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        return self.kSum(nums, target, 4)
    

    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        if not nums:
            # ran out of numbers, no eligible tuples
            return []

        if k == 2:
            # base case is two sum
            return self.twoSum(nums, target)
        
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                # skip over duplicate nums
                continue
            
            # starting with subarray after current element
            # find subsets for (k - 1) sum with subtarget
            subsets = self.kSum(nums[i + 1:], target - nums[i], k - 1)
            for subset in subsets:
                subset.append(nums[i])
                res.append(subset)
        
        return res
        

    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        seen = set()
        for num in nums:
            if res and num == res[-1][1]:
                # skip over duplicate nums
                continue
            n = target - num
            if n in seen:
                res.append([n, num])
            seen.add(num)
        return res
