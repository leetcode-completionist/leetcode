# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums2_str = "".join([chr(num) for num in nums2])
        
        mask = ""
        res = 0
        
        for c in nums1:
            mask += chr(c)
            if mask in nums2_str:
                # match found
                res = max(res, len(mask))
            else:
                # break in subarray
                # popleft from the mask
                mask = mask[1:]
        
        return res
