# https://leetcode.com/problems/break-a-palindrome/
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)

        if n <= 1:
            # impossible
            return ""
        
        has_mid = n % 2 != 0
        mid = n // 2

        for i in range(n):
            if has_mid and i == mid:
                # skip middle char
                continue

            if palindrome[i] != "a":
                # replace first non "a" char with an "a"
                return palindrome[:i] + "a" + palindrome[i + 1:]

        # replace the last char with a "b"
        return palindrome[:-1] + "b"
