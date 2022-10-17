# https://leetcode.com/problems/create-maximum-number/
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def getNums(nums: List[int], target: int) -> List[int]:
            discard = len(nums) - target
            out = []
            
            for num in nums:
                while discard and out and out[-1] < num:
                    out.pop()
                    discard -= 1
                out.append(num)
                
            return out[:target]
          
        def getMax(nums1: List[int], nums2: List[int]) -> List[int]:
            return [max(nums1, nums2).pop(0) for _ in nums1 + nums2]
          
        res = []
        
        for i in range(k + 1):
            if i > len(nums1) or (k - i) > len(nums2):
              # not enough nums from either nums1 or nums2
              continue
              
            a = getNums(nums1, i)
            b = getNums(nums2, k - i)
            res = max(res, getMax(a, b))
        
        return res
