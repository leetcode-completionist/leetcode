# https://leetcode.com/problems/next-greater-element-i/
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_map = {}
        
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            while stack and nums2[i] > nums2[stack[-1]]:
                stack.pop()
            
            if stack:
                next_greater_map[nums2[i]] = stack[-1]
            else:
                next_greater_map[nums2[i]] = -1
                
            stack.append(i)
            
        res = []
        
        for num in nums1:
            if next_greater_map[num] == -1:
                res.append(-1)
            else:
                res.append(nums2[next_greater_map[num]])
            
        return res
