class Solution:
    
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        
        @cache
        def getMinimumDeleteSum(i: int, j: int) -> int:
            if i == m:
                # sum all of s2
                return sum([ord(c) for c in s2[j:]])

            if j == n:
                # sum of all s1
                return sum([ord(c) for c in s1[i:]])

            if s1[i] == s2[j]:
                return getMinimumDeleteSum(i + 1, j + 1)

            return min(
                ord(s1[i]) + getMinimumDeleteSum(i + 1, j),
                ord(s2[j]) + getMinimumDeleteSum(i, j + 1)
            )
        
        return getMinimumDeleteSum(0, 0)
