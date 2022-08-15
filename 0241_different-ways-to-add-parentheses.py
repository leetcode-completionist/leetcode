# https://leetcode.com/problems/different-ways-to-add-parentheses/
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # tokenize the expression into numbers and operators
        tokens = []
        for c in expression:
            if c.isnumeric():
                if tokens and type(tokens[-1]) == int:
                    tokens[-1] *= 10
                    tokens[-1] += int(c)
                else:
                    tokens.append(int(c))
            else:
                tokens.append(c)
        
        # evaluate the expression given two integers and an operation
        def evaluate(a: int, b: int, op: str) -> int:
            if op == "*":
                return a * b
            elif op == "-":
                return a - b
            elif op == "+":
                return a + b
            else:
                raise Exception("illegal operation: {}".format(op))
        
        @cache        
        def dfs(left: int, right: int) -> List[int]:
            if left == right:
                # return the number itself if we ever end up with only one number
                return [tokens[left]]
            if right - left == 2:
                # no way to add more parentheses
                # we will evaluate current subarray
                return [evaluate(tokens[left], tokens[right], tokens[left + 1])]
        
            res = []
            
            # split numbers left and right at every index (that has a number)
            i = left
            while i < right - 1:
                res_left = dfs(left, i)
                res_right = dfs(i + 2, right)
                
                op = tokens[i + 1]
                
                for r_l in res_left:
                    for r_r in res_right:
                        res.append(evaluate(r_l, r_r, op))
            
                # go to the next number
                i = i + 2
            
            return res
        
        return dfs(0, len(tokens) - 1)
