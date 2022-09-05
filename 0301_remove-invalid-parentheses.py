# https://leetcode.com/problems/remove-invalid-parentheses/
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(expr: str) -> bool:
            left = 0
            for c in expr:
                if c not in "()":
                    continue
                
                if c == "(":
                    left += 1
                else:
                    left -= 1
                
                if left < 0:
                    # no way to balance parentheses
                    return False
            
            # check if parentheses are balanced
            return left == 0
        
        res = []
        
        visited = set()
        q = deque([s])
        
        found = False
        while q and not found:
            n = len(q)
            for _ in range(n):
                expr = q.popleft()
                
                if expr in visited:
                    continue
                
                visited.add(expr)
                
                if isValid(expr):
                    res.append(expr)
                    found = True
                    continue
                
                for i in range(len(expr)):
                    if expr[i] not in "()":
                        # not a parentheses, skip
                        continue
                        
                    # remove a parentheses
                    candidate = expr[:i] + expr[i + 1:]
                    q.append(candidate)
        
        return res
