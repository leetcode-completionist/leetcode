class Solution:
    def generateParenthesis(self, n: int) -> List[str]:        
        def generate(s, left, right):
            # recursively builds up possible parenthesis combo
            if not left and not right:
                # valid parenthesis
                res.append(s)
                return
            
            if right < left or left < 0 or right < 0:
                # invalid combo
                return
            
            generate(s + "(", left - 1, right)
            generate(s + ")", left, right - 1)
            
        res = []
        generate("", n, n)
        return res
