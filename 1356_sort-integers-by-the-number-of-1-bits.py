# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        
        nums = defaultdict(list)
        for num in arr:
            nums[bin(num).count("1")].append(num)
            
        res = []
        for k in sorted(nums.keys()):
            res.extend(nums[k])
        return res
