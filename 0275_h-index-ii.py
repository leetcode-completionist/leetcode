# https://leetcode.com/problems/h-index-ii/
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        This question is very similar to h-index I
        (https://leetcode.com/problems/h-index/).
        
        Since the input is already sorted, we can skip
        O(nlog(n)) sort phase. However, the array is in
        increasing order. So our previous logic has to
        be flipped (e.g. rather than nums[i] >= i, we have
        nums[i] >= len(nums) - i)
        
        We want to find the index of the first element
        where nums[i] < len(nums) - i.
        """
        n = len(citations)
        
        l, r = 0, n - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if citations[mid] >= n - mid:
                r = mid - 1
            else:
                l = mid + 1
            
        return n - l
