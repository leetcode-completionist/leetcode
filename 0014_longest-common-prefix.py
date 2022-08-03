class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # use first element as possible prefix
        res = strs[0]
        
        for s in strs[1:]:
            # iterate through the shorter string
            for i in range(min(len(res), len(s))):
                # trim prefix to matching chars
                if res[i] != s[i]:
                    res = res[:i]
                    break
            # trim prefix to shorter string
            res = res[:min(len(res), len(s))]
            
        return res
