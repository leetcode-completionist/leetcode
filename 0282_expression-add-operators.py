# https://leetcode.com/problems/expression-add-operators/
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        
        res = []
        
        def dfs(i: int, expr: List[str], val, prev):
            if i == n:
                if val == target:
                    res.append("".join(expr))
                return
        
            for j in range(i, n):
                operand_s = num[i:j + 1]
                operand_i = int(operand_s)
                
                if not expr:
                    # we are reading the first number
                    # so we do not add any operators yet
                    dfs(j + 1, [operand_s], operand_i, operand_i)
                    
                else:
                    dfs(j + 1, expr + ["+"] + [operand_s], val + operand_i, operand_i)
                    dfs(j + 1, expr + ["-"] + [operand_s], val - operand_i, -operand_i)
                    
                    # when we DFS with a multiply, we need to "undo" a previous calculation
                    dfs(j + 1, expr + ["*"] + [operand_s], val - prev + operand_i * prev, operand_i * prev)
                    
                if num[i] == "0":
                    # we only want to dfs ONCE if we are
                    # currently reading a zero.
                    #
                    # for example 0 + 0 + 1 is valid
                    # however, 00 + 1 is not valid
                    break
        
        dfs(0, [], 0, 0)
        
        return res
