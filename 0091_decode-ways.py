class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        dp = [0] * n
        dp.append(1) # handles the last element edge case
        
        for i in range(n - 1, -1, -1):
            # print(dp)
            if s[i] == "0":
                # can't decode with a leading "0"
                continue
                
            # we have at least one way of decoding
            # plus the num of decodings for s[i + 1:]
            dp[i] = dp[i + 1]
            
            # if s[i:i+2] is also a valid decoding
            # we will add num of decodings for s[i + 2:]
            # to current cell in dp
            if i < n - 1 and int(s[i:i+2]) < 27:
                dp[i] += dp[i + 2]
        
        # first cell contains total number of decodings from
        # the first letter
        return dp[0]
