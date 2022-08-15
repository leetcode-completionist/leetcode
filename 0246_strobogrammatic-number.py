# https://leetcode.com/problems/strobogrammatic-number/
class Solution:
    
    # this is heavily based on the quesiton's assumptions
    # for example, 1 might not be strobogrammatic for
    # certain fonts. And 2 might be considered strobogrammatic
    # for other fonts.
    STROBOGRAMMATIC_NUMS = {
        "0": "0",
        "1": "1",
        "6": "9",
        "8": "8",
        "9": "6"
    }
    
    def isStrobogrammatic(self, num: str) -> bool:
        rev = ""
        
        for c in num:
            if c not in Solution.STROBOGRAMMATIC_NUMS:
                return False
            
            # we always add to the front because
            # when the original number is flipped 180
            # its numbers are also in reversed order.
            rev = Solution.STROBOGRAMMATIC_NUMS[c] + rev
            
        return rev == num
