class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        l, r = 0, len(s) - 1
        while l < r:
            c_l = ord(s[l])
            c_r = ord(s[r])
            
            # keep shrinking the window if non-alpha chars
            if (c_l < ord("0") or
                c_l > ord("z") or
                (ord("9") < c_l < ord("a"))):
                l += 1
                continue

            if (c_r < ord("0") or
                c_r > ord("z") or
                (ord("9") < c_r < ord("a"))):
                r -= 1
                continue
                
            if c_l != c_r:
                return False

            l += 1
            r -= 1
            
        return True
