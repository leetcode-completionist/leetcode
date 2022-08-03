class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # removes leading and trailing spaces
        s = s.strip()
        
        # iterate from the back of string until we
        # come across the first space
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                return len(s) - 1 - i

        return len(s)
