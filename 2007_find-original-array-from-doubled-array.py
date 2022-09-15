# https://leetcode.com/problems/find-original-array-from-doubled-array/
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            # odd length arrays cannot be doubled arrays
            return []
        
        # create a freq map of each num
        freq = defaultdict(int)
        for num in changed:
            freq[num] += 1
        
        # sort num in increasing order
        changed.sort()
        
        res = []
        
        for num in changed:
            if not freq[num]:
                # num was previously used as another num's double
                continue
            
            double = num * 2
            if double not in freq or not freq[double]:
                # not a doubled array
                return []
            
            freq[num] -= 1
            freq[double] -= 1
            res.append(num)
        
        return res
