# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool: 
        # we keep track of a lower bound to make sure
        # new elements never go below the bound.
        lower_bound = 0
        
        # simulates a DFS recursion stack
        stack = []
        
        for val in preorder:
            if val < lower_bound:
                # invalid BST
                return False
                
            # if current val is larger than the previous val,
            # we remove from stack and make it our new boundary
            while stack and val > stack[-1]:
                lower_bound = stack.pop()
            
            # current val can be added to the stack
            stack.append(val)
        
        return True
