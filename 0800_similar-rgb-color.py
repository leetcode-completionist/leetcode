# https://leetcode.com/problems/similar-rgb-color/
class Solution:
    
    HEX_CHARS = [
        "00", "11", "22", "33", "44", "55", "66", "77", "88", "99",
        "aa", "bb", "cc", "dd", "ee", "ff"
    ]
    
    def similarRGB(self, color: str) -> str:
        @cache
        def nearest(target: str) -> str:
            target_code = int(target, 16)
            res = (math.inf, "00")
            for cand in Solution.HEX_CHARS:
                res = min(res, (abs(target_code - int(cand, 16)), cand))
            return res[-1]

        res = "#"
        res += nearest(color[1:3])  # nearest R
        res += nearest(color[3:5])  # nearest G
        res += nearest(color[5:])   # nearest B
        
        return res
