class Solution:
    def evalRPN(self, tokens: List[str]) -> int:        
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() +
                             stack.pop())
            elif token == "-":
                stack.append(-(stack.pop() -
                             stack.pop()))
            elif token == "*":
                stack.append(stack.pop() *
                             stack.pop())
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                if not (b < 0) == (a < 0):
                    # not positive, use abs values
                    # then add back the negative sign
                    stack.append(-(abs(a)//abs(b)))
                else:
                    stack.append(a//b)
            else:
                stack.append(int(token))
                
        return stack[-1]
