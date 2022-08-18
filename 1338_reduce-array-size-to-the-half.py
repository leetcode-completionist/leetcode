# https://leetcode.com/problems/reduce-array-size-to-the-half/
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = defaultdict(lambda: 0)
        for num in arr:
            freq[num] += 1
        
        n = math.ceil(len(arr) / 2)
        
        freq_arr = sorted(freq.values())
        
        res = 0
        while freq_arr:
            count = freq_arr.pop()
            n -= count
            res += 1
            
            if n <= 0:
                return res
        return res
