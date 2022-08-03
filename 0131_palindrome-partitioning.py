class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = []
        for i in range(len(s)):
            dp.append([])
        dp.append([[]])
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s) + 1):
                if self.isPalindrome(s[i:j]):
                    for r in dp[j]:   
                        dp[i].append([s[i:j]] + r)
        
        return dp[0]
                
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
