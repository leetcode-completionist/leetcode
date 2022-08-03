class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        
        # keep track of total "L" and "R"
        s_l_total, t_l_total = 0, 0
        s_r_total, t_r_total = 0, 0
        
        # keep track of running "L" and "R"
        # we will reset to zero if we
        # come across a "barrier"
        # 
        # i.e. "L" cannot go further left if
        # there is an "R" in the way
        s_l, t_l = 0, 0
        s_r, t_r = 0, 0
        
        # single pass
        for i in range(n):
            # from right to left
            if target[n - i - 1] == "L":
                t_l += 1
                t_l_total += 1
            elif target[n - i - 1] == "R":
                # reset t_l because it cannot go past any "R"
                t_l = 0
                
            if start[n - i - 1] == "L":
                s_l += 1
                s_l_total += 1
            elif start[n - i - 1] == "R":
                # reset s_l because it cannot go past any "R"
                s_l = 0
                
            if s_l < t_l:
                # if at any point, the running count
                # of s_l is less than t_l
                # we know it is impossible
                return False
            
            # from left to right
            if target[i] == "L":
                # reset t_r because it cannot go past any "L"
                t_r = 0
            elif target[i] == "R":
                t_r += 1
                t_r_total += 1
                
            if start[i] == "L":
                # reset t_r because it cannot go past any "L"
                s_r = 0
            elif start[i] == "R":
                s_r += 1
                s_r_total += 1
                
            if s_r < t_r:
                # if at any point, the running count
                # of s_r is less than t_r
                # we know it is impossible
                return False
        
        return s_l_total == t_l_total and s_r_total == t_r_total
