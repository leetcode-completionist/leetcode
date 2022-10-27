# https://leetcode.com/problems/image-overlap/
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        m, n = len(img1), len(img1[0])
        
        img1_bits = []
        img2_bits = []
        for i in range(m):
            for j in range(n):
                if img1[i][j] == 1:
                    img1_bits.append((i, j))
                if img2[i][j] == 1:
                    img2_bits.append((i, j))
        
        overlaps = defaultdict(int)
        
        res = 0
        for img1_i, img1_j in img1_bits:
            for img2_i, img2_j in img2_bits:
                overlap = (img1_i - img2_i, img1_j - img2_j)
                overlaps[overlap] += 1
                res = max(res, overlaps[overlap])
        return res
