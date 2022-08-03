class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # We use bits to keep track of nums seen
        #
        # The problem states that 1 element will only
        # occur onces, while all other elements will
        # occur exactly twice
        xor = 0
        
        for num in nums:
            # num XOR num will equal 0 because every bit will be the same.
            # A number that only occurs once will leave its bits on
            #    
            # Additionally, ordering of elements does
            # not matter in XOR, for example:
            #
            #   a^b^c^b^c == b^b^c^c^a
            #
            # As a result, we can keep XOR nums as we encounter them and
            # can be sure that at the end, only one num will remain
            xor ^= num
        return xor
