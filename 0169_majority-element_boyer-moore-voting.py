class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        This solution implements the Boyer-Moore
        Voting Algorithm.
        
        At a high level:
        
        1. Keep an ongoing candidate for majority
        
        2. Keep track of candidate's votes with +1 and -1
        
        3. Whenever vote is 0 (i.e. no current majority),
           the current number can become a candidate
           
        4. We can safely ignore previously seen votes
           because we would've discared an equal number
           of majority votes vs. non-majority votes.
           
           This ensure we will still have a majority
           element in the array moving forward.
        """
        candidate = None
        vote = 0
        
        for num in nums:
            if vote == 0:
                # if there is no current majority
                # take over as the candidate
                candidate = num
            
            # increase the vote if same as
            # previous candidate
            if candidate == num:
                vote += 1
            else:
                # else decrease the vote
                vote -=1
        
        return candidate
                    
