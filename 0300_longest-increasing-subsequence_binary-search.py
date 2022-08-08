class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        This solution attempts to build up seq array
        that contains the length of LIS
        (but not necessarily the exact sequence itself)
        
            Given [10,9,2,5,3,7,101,18]

            i = 0, seq = [10]
            i = 1, 9 < 10, seq = [9]
            i = 2, 2 < 9, seq = [2]
            i = 3, 5 > 2, seq = [2,5]
            i = 4, 3 < 5, seq = [2,3]
            i = 5, 7 > 3, seq = [2,3,7]
            i = 6, 101 > 7, seq = [2,3,7,101]
            i = 7, 18 < 101, seq = [2,3,7,18]
        
        At each iteration, we swap in any lower value into the seq
        to maximize sequence length. Using binary search, this
        reduces our runtime to O(nlog(n)).
        """
        seq = [nums[0]]
        
        for num in nums[1:]:
            if num > seq[-1]:
                seq.append(num)
            else:
                # find where we should insert
                # this number
                i = bisect_left(seq, num)
                
                # swap out the number
                seq[i] = num
        
        return len(seq)
