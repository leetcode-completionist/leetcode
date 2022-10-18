# https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        res = set(nums)
        
        for num in nums:
            s = str(num)[::-1]
            res.add(int(s.lstrip("0")))
            
        return len(res)
