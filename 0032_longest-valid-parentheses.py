class Solution:    
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        
        res = 0
        
        # Initialize stack with -1 so we can always pop
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                # left parenthesis always append current index
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # move index up to current to restart count
                    stack.append(i)
                else:
                    l = i - stack[-1]
                    res = max(l, res)

        return res
