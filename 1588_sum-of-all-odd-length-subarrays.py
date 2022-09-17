# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        prev = 0
        for i in range(n):
            # There are (i + 1) // 2 odd arrays to the left
            # but we've already calculated those from a prior number
            # so we subtract the count from previous
            left = prev - (i + 1) // 2
            right = (n - i + 1) // 2
            
            res += arr[i] * (left + right)
            
            prev = left + right
        return res
