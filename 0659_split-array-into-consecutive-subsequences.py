# https://leetcode.com/problems/split-array-into-consecutive-subsequences/
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        # track subsequences that can end on an index
        subseq = defaultdict(int)
        
        for num in nums:
            if not freq[num]:
                # we already used this number for a
                # subsequence
                continue
            
            # we are using up this num, so we remove it from freq
            freq[num] -= 1
            
            # we greedily check if we can add to an existing
            # subsequence. If not, we greedily initiates a
            # new subsequence of length 3 (while consuming it from
            # the frequency table)
            #
            # If we are unable to do neither of the above, it is
            # not possible to split this array into consecutive
            # subsequences.
            
            if subseq[num - 1]:
                # there is an existing subsequence
                # move the subsequence to the new number
                subseq[num - 1] -= 1
                subseq[num] += 1
            
            elif freq[num + 1] and freq[num + 2]:
                # see if we have minimal nums to
                # for a subsequence
                # set a new subsequence at num + 2
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                subseq[num + 2] += 1
                 
            else:
                return False
            
        return True
