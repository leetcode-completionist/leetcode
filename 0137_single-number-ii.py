class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # once  = (NOT in twice) AND (in Once)        
        once = 0
        
        # twice = (NOT in once) AND (in Twice)
        twice = 0

        for num in nums:
            # 1 occurrance will set bits in once, not in twice
            # 2 occurrance will clear bits in once, and set bits in twice
            # 3 occurrance will set bits in once, clear bits in twice
            once = ~twice & (once ^ num)
            twice = ~once & (twice ^ num)

        return once
