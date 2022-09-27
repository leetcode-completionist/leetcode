# https://leetcode.com/problems/push-dominoes/
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # There are only 4 states to consider:
        #
        #   L...L -> LLLLL
        #   R...R -> RRRRR
        #   L...R -> L...R
        #   R...L -> RR.LL
        #
        # We start by padding the beginning with "L"
        # and end with "R"
        #
        # This doesn't change the final answer in
        # between, and it simplifies the implementation
        # by avoiding edge case handling
        # (i.e. left/right edge).
        dominoes = "L" + dominoes + "R"

        # Locating all the initially
        # pushed dominoes.
        pushed = []
        for i, domino in enumerate(dominoes):
            if domino != ".":
                pushed.append(i)

        # String is not mutable, we create a
        # list of chars.
        dominoes_list = list(dominoes)
            
        # look at each range and modify dominoes_list
        # accordingly
        for l, r in zip(pushed, pushed[1:]):
            if l == r - 1:
                # no vertical dominoes in between
                continue
            
            left, right = dominoes[l], dominoes[r]

            if (c := left) == right:
                # L...L -> LLLLL
                # R...R -> RRRRR
                #
                # Both sides are equal. Fill in the
                # middle with the same character.
                for i in range(l + 1, r):
                    dominoes_list[i] = c
            
            elif left == "L" and right == "R":
                # L ... R
                #
                # Dominoes in between are unchanged.
                continue
            
            elif left == "R" and right == "L":
                # determine the midpoint
                m = l + (r - l) // 2

                # determine if our current range is even length
                # or odd
                even = (r - l + 1) % 2 == 0
                
                # R...L -> RR...
                for i in range(l + 1, m + (1 if even else 0)):
                    dominoes_list[i] = left
                
                # R...L -> ...LL
                for i in range(r - 1, m, -1):
                    dominoes_list[i] = right
        
        # form a string and strip the left/right padding
        dominoes = "".join(dominoes_list)
        dominoes = dominoes[1:]
        dominoes = dominoes[:-1]
        
        return dominoes
