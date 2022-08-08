class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        
        l, r = 0, 0
        while r <= len(s):
            if r == len(s) or s[r] == " ":
                # reverse our previous word
                swap_l, swap_r = l, r - 1
                while swap_l < swap_r:
                    s[swap_l], s[swap_r] = s[swap_r], s[swap_l]
                    swap_l += 1
                    swap_r -= 1
                l = r + 1
                r = r + 1
            else:
                r += 1
