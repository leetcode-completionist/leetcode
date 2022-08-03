class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            # window is larger than s, impossible
            return ""
        
        # keep track of substring requirements
        req = Requirement()
        for c in t:
            req.addReq(c)

        res = ""
        
        # initialize with first char of s
        req.see(s[0])
        
        # while our window hasn't reached the end yet
        l, r = 0, 0
        while r < len(s):
            if req.is_okay():
                # no more required chars left
                if not res or len(res) > (r - l + 1):
                    # check if matched substring is smaller
                    res = s[l:r + 1]
                # shrink window by moving left pointer
                req.unsee(s[l])
                l += 1
                # keep shrinking window until we come across
                # a required char
                while l < r and s[l] not in req.freq:
                    l += 1
            else:
                if r == len(s) - 1:
                    # we have reached the end, break out
                    break
                # expand window by moving right pointer
                r += 1
                # keep expanding until we come across
                # a required char
                while r < len(s) - 1 and s[r] not in req.freq:
                    r += 1
                req.see(s[r])
                
        return res

    
class Requirement:
    def __init__(self) -> None:
        self.freq = {}
        self.formed = 0
        self.required = 0
        
        
    def is_okay(self):
        return self.formed == self.required
        
        
    def addReq(self, c: str) -> None:
        if c not in self.freq:
            self.freq[c] = 0
            self.required += 1
        self.freq[c] += 1

        
    def see(self, c: str) -> None:
        if c not in self.freq:
            # ignore unnecessary chars
            return

        self.freq[c] -= 1
        if self.freq[c] == 0:
            # dropped to zero so we have a newly
            # formed letter
            self.formed += 1
        
        
    def unsee(self, c: str) -> None:
        if c not in self.freq:
            # ignore unnecessary chars
            return

        self.freq[c] += 1
        if self.freq[c] == 1:
            # increased to 1 so we have no longer
            # have a formed letter
            self.formed -= 1
