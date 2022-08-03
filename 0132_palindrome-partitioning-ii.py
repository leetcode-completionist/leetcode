class Solution:
    def minCut(self, s: str) -> int:
        if not s:
            return False

        if s == s[::-1]:
            # already a palindrome, no cut needed
            return 0
        
        dp = [float("inf")] * len(s)
        dp.append(0)
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s) + 1):
                if self.isPalindrome(s[i:j]):
                    dp[i] = min(dp[i], 1 + dp[j])
                        

        return dp[0] - 1
                
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        return s == s[::-1]
