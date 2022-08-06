class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:        
        if s == t:
            return False
        
        m, n = len(s), len(t)
        
        i, j = 0, 0
        edit = False
        while i < m and j < n:
            if s[i] == t[j]:
                # matching char, no edit needed
                i += 1
                j += 1
                continue
        
            if edit:
                # we already made one edit
                return False
        
            # we will make one edit
            edit = True
            
            if m < n:
                # s is shorter, we can insert
                j += 1

            elif m > n:
                # s is longer, we can delete
                i += 1

            else:
                # same length, we can replace
                i += 1
                j += 1
        
        # check that we've reached the end of both strings
        #
        # OR
        #
        # check that we are at the last character of either string
        # and we haven't made any edits so far. This means that
        # all the characters have been the same so far and one string
        # is longer than the other.
        return ((i == m - 1 or j == n - 1) and not edit) or (i == m and j == n)
