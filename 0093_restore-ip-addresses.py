class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)

        # Prune invalid branches
        if n > 12:
            # does not meet max IP length (e.g. 255.255.255.255)
            return res
        if n < 4:
            # does not meet min IP length (e.g. 0.0.0.0)
            return res
        
        @cache
        def dfs(i: int, dot: int) -> List[str]:
            if i == n:
                # we got to the end
                return []
            
            if not dot:
                # We used up our dots. Check if remaining str
                # is a valid integer.
                if i == n - 1:
                    # all single integers (0,..., 9) are valid
                    return [s[i]]
                
                if s[i] == "0":
                    # integers cannot have leading zeros
                    return []
                
                if int(s[i:]) > 255:
                    # integer out of valid range
                    return []
                
                return [s[i:]]

            res = []
            
            # we can always look at the next digit
            if i < n - 1:
                for ip in dfs(i + 1, dot - 1):
                    res.append(s[i] + "." + ip)
            
            if s[i] == "0":
                # we cannot go further because integers
                # cannot start with a zero
                return res
            
            # otherwise we can continue to expand
            if i < n - 1:
                for ip in dfs(i + 2, dot - 1):
                    res.append(s[i:i+2] + "." + ip)

            # we can look at 2 digits to the right IFF
            # we can still be in range (i.e. under 256)
            if i < len(s) - 2 and int(s[i:i+2]) <= 25:
                for ip in dfs(i + 3, dot - 1):
                    res.append(s[i:i+3] + "." + ip)

            return res
        
        # start at i=0 with 3 dots
        return dfs(0, 3)
