# https://leetcode.com/problems/orderly-queue/
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            # rotation only, no out of order sorting
            return min(s[i:] + s[:i] for i in range(len(s)))
            
        # else, we can take as many moves as it needs
        # to get to the smallest string
        return "".join(sorted(s))
