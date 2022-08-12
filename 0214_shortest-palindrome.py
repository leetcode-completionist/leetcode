class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            # string is already a palindrome
            return s
        
        for i in range(len(s) - 1, -1, -1):
            # greedily detect if we have a palindrome from
            # the beginning of string
            if s[:i + 1] == s[:i + 1][::-1]:
                # we will add the non-palindrome suffix in
                # reverse as the prefix
                return s[i + 1:][::-1] + s
            
        # we should never get here
        raise Exception("illegal state")
