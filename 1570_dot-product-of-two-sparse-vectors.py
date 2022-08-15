# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
class SparseVector:
    def __init__(self, nums: List[int]):
        # we can ignore all zeroes and store
        # index to non-zero values
        self.vec_map = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.vec_map[i] = num

                
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        
        # we pick the shorter hashmap to loop over
        short, long = vec.vec_map, self.vec_map
        if len(short) > len(long):
            short, long = long, short
        
        for k, v in short.items():
            if k in long:
                res += v * long[k]
        
        return res


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
