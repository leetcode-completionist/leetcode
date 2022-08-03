class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        res = 0
        for num in nums_set:
            if num - 1 in nums_set:
                # there is a number smaller
                # so current number cannot
                # be the start of a sequence
                continue
            
            # start of a sequence, iterate until end of sequence
            seq = 0
            while num in nums_set:
                seq += 1
                num += 1
            
            res = max(res, seq)
        return res
