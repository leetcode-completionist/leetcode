class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        
        dp = [0] * n
        
        diffs = defaultdict(list)
        
        res = 1
        for i in range(n - 1, -1, -1):
            num = arr[i]
            
            diffs[num - difference].append(i)
            dp[i] = 1
            
            if num not in diffs:
                continue
                        
            for next_num in diffs[num]:
                if next_num != i:
                    # Not self
                    # Edge case when difference == 0
                    dp[i] = max(dp[i], dp[next_num] + 1)

            res = max(res, dp[i])
            
        return res
