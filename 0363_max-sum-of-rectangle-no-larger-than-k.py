# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/
from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        res = -math.inf
        
        m, n = len(matrix), len(matrix[0])

        # ensure that cols < rows, otherwise transpose the matrix
        if m < n:
            matrix = list(zip(*matrix))
            m, n = n, m
        
        # for each column
        for col in range(n):
            
            prefix_sums = [0] * m

            for j in range(col, n):
                # add current column into the prefix sum array
                for i in range(m):
                    prefix_sums[i] += matrix[i][j]
                
                res = max(res, self.maxSumSubarray(prefix_sums, k))
                if res == k:
                    return res
        
        return res
        
        
    def maxSumSubarray(self, nums: List[int], k: int) -> int:
        # create a sorted list of all prefix sums.
        # this allows us to look up desired prefixes
        # in O(log(n)) instead of O(n)
        prefix = SortedList([0])
                
        res = -math.inf
        
        # we keep a running sum of every element we've seen.
        # this allows us to extract a sub-array by simply
        # subtracting a previously recorded prefix from the running sum
        #
        #         [A,   B,     C,       D]
        # prefix  [A, A+B, A+B+C, A+B+C+D]
        #
        # If we want [C,D] and our running sum is (A+B+C+D)
        # Then we should subtract (A+B) from running sum to get (C+D).
        curr_sum = 0
        
        for num in nums:
            curr_sum += num
            
            # find the largest prefix that satisfies (curr_sum - k)
            i = prefix.bisect_left(curr_sum - k)
            if i < len(prefix):
                res = max(res, curr_sum - prefix[i])
                
            # add curr_sum to prefix_sum
            prefix.add(curr_sum)
        
        return res
