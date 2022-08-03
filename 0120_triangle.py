class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # initialize DP with an empty row
        triangle.append([0] * (len(triangle[-1]) + 1))
        
        # start from the second to last row
        # because of our empty bottom row
        for i in range(len(triangle) - 2, -1, -1):
            curr = triangle[i]
            prev = triangle[i + 1]
            
            for j in range(len(curr)):
                # add the minimum of the adjacent numbers
                curr[j] += min(prev[j], prev[j + 1])
        
        # the min path sum is bubbled up to the first row (1 cell)
        return triangle[0][0]
