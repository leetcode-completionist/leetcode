# https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_m = {}
        for num in nums1:
            if num not in nums1_m:
                nums1_m[num] = 1
            else:
                nums1_m[num] += 1

        nums2_m = {}
        for num in nums2:
            if num not in nums2_m:
                nums2_m[num] = 1
            else:
                nums2_m[num] += 1
                
        res = []
        
        for k, v in nums1_m.items():
            if k not in nums2_m:
                continue
            res += [k] * min(v, nums2_m[k])
        
        return res
