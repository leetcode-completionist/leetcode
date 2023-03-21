class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        
        count = 0
        for num in nums:
            if num == 0:
                # continue to expand subarray
                count += 1
            elif count > 0:
                # add number of subarrays seen so far
                res += self.numberOfSubarrays(count)        
                count = 0
                
        if count > 0:
            # check trailing zero subarrays
            res += self.numberOfSubarrays(count) 
            count = 0

        return res
        
        
    def numberOfSubarrays(self, count: int) -> int:
        # sum of natural numbers 1 ... count
        return int(count * (count + 1) / 2)
