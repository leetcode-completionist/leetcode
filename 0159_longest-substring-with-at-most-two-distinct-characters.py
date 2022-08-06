class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        res = 0
        
        l, r = 0, 0
        seen = {s[0]: 1}
        while r < len(s) - 1:
            # expand window until we have more
            # than two distinct characters
            while len(seen.keys()) < 3:
                # keep track of max length while
                # we are here
                res = max(res, r - l + 1)
                
                if r == len(s) - 1:
                    # we can't expand any further
                    break
                
                r += 1
                add = s[r]
                if add not in seen:
                    seen[add] = 1
                else:
                    seen[add] += 1
            
            # shrink window until we have
            # at most two distinct characters
            while len(seen.keys()) > 2:
                remove = s[l]
                l += 1

                seen[remove] -= 1
                if seen[remove] == 0:
                    del seen[remove]
                    
        return res
