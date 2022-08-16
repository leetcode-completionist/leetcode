# https://leetcode.com/problems/strobogrammatic-number-ii/
class Solution:
    
    SINGLES = ["0", "1", "8"]
    
    PAIRS = ["00", "11", "69", "88", "96"]
    
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 1:
            return Solution.SINGLES
        
        def find(i: int) -> List[str]:
            if i == 1:
                # base case
                return Solution.SINGLES
            
            if i == 2:
                # base case
                # we don't use leading zeroes at the top level
                return Solution.PAIRS if i != n else Solution.PAIRS[1:]
                    
            # we know in order for a number to be strobogrammatic,
            # left num and right num needs to be a pair.
            #
            # For example, if n = 5, then our string will look
            # something like:
            #
            #     0###0, 1###1, 6###9, 8###8, 9###6
            #
            # To figure out what is inside (i.e. #'s), we need to
            # lookup all possible strobogrammatic numbers for n = 3:
            #
            #     0#0, 1#1, 6#9, 8#8, 9#6
            #
            # Notice that to find all numbers for n = 3, we will need
            # to know all possible strobogrammatic numbers for n = 1.
            #
            # To summarize, our recurrance formula will be:
            #
            #     find(n) = find(n - 2) X strobogrammatic_pairs
            #
            # Where all results from find(n - 2) will be wrapped
            # around by each strobogrammatic pairs.
            res = []
            
            # we don't use leading zeroes at the top level
            pairs = Solution.PAIRS if i != n else Solution.PAIRS[1:]
            
            for pair in pairs:
                for s in find(i - 2):
                    res.append(pair[0] + s + pair[1])
            
            return res
            
        return find(n)
