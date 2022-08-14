class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        seen = defaultdict(lambda: 0)
        
        for num in nums:
            seen[num] += 1
        
        res = []
        
        req = len(nums) // 3
        for k, v in seen.items():
            if v > req:
                res.append(k)
        return res
