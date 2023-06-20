class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        res = alt
        
        for num in gain:
            alt += num
            res = max(res, alt)
        
        return res
