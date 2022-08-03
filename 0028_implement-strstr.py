class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_length = len(haystack)
        needle_length = len(needle)
        
        if haystack_length == needle_length:
            return 0 if haystack == needle else -1
        
        for i in range(haystack_length - needle_length + 1):
            if haystack[i:i + needle_length] == needle:
                return i

        return -1
