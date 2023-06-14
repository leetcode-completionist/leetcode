class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        nums.sort()
        
        res = set()
        
        for i in range(n - 1):
            a = nums[i]
            
            target = a + k
            
            j = bisect.bisect_left(a=nums, x=target, lo=i + 1)

            if j >= n:
                continue
                
            if nums[j] == target:
                res.add(
                    (
                        min(nums[i], nums[j]),
                        max(nums[i], nums[j]),
                    ),
                )
        
        return len(res)
