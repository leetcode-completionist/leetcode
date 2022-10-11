# https://leetcode.com/problems/maximum-product-of-word-lengths/
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mask_to_length = defaultdict(int)
        for word in words:
            # create bitmask
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord("a"))

            # pick the longest length for a mask
            mask_to_length[mask] = max(len(word), mask_to_length[mask])
        
        res = 0
        for mask, length in mask_to_length.items():
            for other, other_length in mask_to_length.items():
                if mask == other:
                    continue
                if mask & other == 0:
                    res = max(res, length * other_length)
        return res
