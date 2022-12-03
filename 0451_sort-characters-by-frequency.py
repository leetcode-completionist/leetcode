# https://leetcode.com/problems/sort-characters-by-frequency/
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        
        l = [(count, char) for char, count in freq.items()]
        l.sort(key=lambda x: -x[0])
        
        res = [(tup[1] * tup[0]) for tup in l]
        return "".join(res)
