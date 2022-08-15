# https://leetcode.com/problems/different-ways-to-add-parentheses/
class Solution:
    # evaluate the expression given two integers and an operation
    def evaluate(self, a: int, b: int, op: str) -> int:
        if op == "*":
            return a * b
        elif op == "-":
            return a - b
        elif op == "+":
            return a + b
        else:
            raise Exception("illegal operation: {}".format(op))
    
    
    @cache
    def diffWaysToCompute(self, expression: str) -> List[int]:       
        if expression.isdigit():
            return [int(expression)]
        
        res = []
        
        for i, c in enumerate(expression):
            if c in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                op = expression[i]
                for l in left:
                    for r in right:
                        res.append(self.evaluate(l, r, op))
        
        return res
