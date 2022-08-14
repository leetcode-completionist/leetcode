# https://leetcode.com/problems/summary-ranges/
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        
        for num in nums:
            if not ranges:
                ranges.append([num])
            elif num > ranges[-1][-1] + 1:
                # new range
                ranges.append([num])
            elif len(ranges[-1]) == 1:
                # make a single num into a range
                ranges[-1].append(num)
            else:
                # update the end of the range
                ranges[-1][-1] = num
        
        res = []
        for r in ranges:
            res.append("->".join([str(i) for i in r]))
        return res
