# https://leetcode.com/problems/h-index/
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # sort citations in reverse order
        citations.sort(reverse=True)
        
        h_index = 0
        for i in range(len(citations)):
            if i + 1 > citations[i]:
                # current citation doesn't have enough
                # cites to keep up with the h-index
                # return the h-index
                return h_index
            
            # h_index can continue to grow
            h_index += 1
        
        return h_index
