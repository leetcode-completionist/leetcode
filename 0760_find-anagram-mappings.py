class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx = defaultdict(list)
        for i, num in enumerate(nums2):
            idx[num].append(i)
            
        res = []
        for num in nums1:
            res.append(idx[num].pop())
        return res
