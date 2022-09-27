# https://leetcode.com/problems/push-dominoes/
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # pad left/right to avoid edge case handling
        dominoes = "L" + dominoes + "R"

        # find already pushed dominoes
        pushed = []
        for i, domino in enumerate(dominoes):
            if domino != ".":
                pushed.append(i)

        # conver to str mutable char list
        dominoes_list = list(dominoes)
            
        # for each range in between already pushed dominoes
        for l, r in zip(pushed, pushed[1:]):
            if l == r - 1:
                # no vertical dominoes in range
                continue
            
            left, right = dominoes[l], dominoes[r]

            if (c := left) == right:
                # fill range with same char
                for i in range(l + 1, r):
                    dominoes_list[i] = c
            
            elif left == "L" and right == "R":
                # do nothing
                continue
            
            elif left == "R" and right == "L":
                m = l + (r - l) // 2
                even = (r - l + 1) % 2 == 0
                
                # fill left side
                for i in range(l + 1, m + (1 if even else 0)):
                    dominoes_list[i] = left
                
                # fill right side
                for i in range(r - 1, m, -1):
                    dominoes_list[i] = right
        
        # strip the left/right padding and return results
        return "".join(dominoes_list[1:-1])
