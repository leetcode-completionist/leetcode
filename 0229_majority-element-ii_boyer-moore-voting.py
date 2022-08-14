# https://leetcode.com/problems/majority-element-ii/
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # "majority" is defined by the problem as any item with
        # len(nums) // 3 votes
        #
        # this means there can be AT MOST 2 majority elements
        # 
        # With this, we can apply Boyer-Moore Voting Algorithm
        # (https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm)
        # by keeping track of 2 pointers.
        #
        # by the end of the array, we will have at least 1 possible
        # majority element. However, there is no guarantee the chosen element
        # indeed meets our requirement.
        #
        # before we return, we still need to double check the candidate
        # indeed meets the len(nums) // 3 votes requirement
        candidate_1, candidate_1_count = None, None
        candidate_2, candidate_2_count = None, None
        
        for num in nums:
            if candidate_1 is None:
                candidate_1 = num
                candidate_1_count = 1
                
            elif candidate_1 == num:
                candidate_1_count += 1
                
            elif candidate_2 is None:
                candidate_2 = num
                candidate_2_count = 1
            
            elif candidate_2 == num:
                candidate_2_count += 1
                
            elif candidate_1_count == 0:
                candidate_1 = num
                candidate_1_count = 1
                
            elif candidate_2_count == 0:
                candidate_2 = num
                candidate_2_count = 1

            else:
                candidate_1_count -= 1
                candidate_2_count -= 1
            
        real_candidate_1_count = 0
        real_candidate_2_count = 0
        
        for num in nums:
            if num == candidate_1:
                real_candidate_1_count += 1
            elif num == candidate_2:
                real_candidate_2_count += 1
                
        res = []
        
        requirement = len(nums) // 3
        
        if real_candidate_1_count > requirement:
            res.append(candidate_1)
        
        if real_candidate_2_count > requirement:
            res.append(candidate_2)
            
        return res
