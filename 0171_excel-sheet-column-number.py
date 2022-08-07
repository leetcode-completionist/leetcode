class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0

        for i, c in enumerate(columnTitle[::-1]):
            n = ord(c) - ord("A") + 1
            res += n * 26**i
            
        return res
