class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # start from the back
        i = m + n - 1
        
        # pointer to nums1 from the back
        j = m - 1
        
        # pointer to nums2 from the back
        k = n - 1
        
        # iterate until we build a decreasing list
        # from the back
        while j >= 0 and k >= 0:
            if nums1[j] > nums2[k]:
                nums1[i] = nums1[j]
                j -= 1
            else:
                nums1[i] = nums2[k]
                k -= 1
            i -=1
            
        # if we exhaust integers from nums2
        # then we have a sorted list
        # because we can assume elements to the left of i
        # are already smaller than all integers in nums2
        while k >= 0:
            # otherwise, we will put integers from nums2
            # into nums1 until there are no more nums2
            nums1[i] = nums2[k]
            i -= 1
            k -= 1
