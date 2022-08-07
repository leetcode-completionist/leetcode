class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = defaultdict(lambda: 0)
        for num in nums:
            seen[num] += 1
        
        for k, v in seen.items():
            if v > len(nums) // 2:
                return k
        
        raise Exception("illegal test case")
