# https://leetcode.com/problems/basic-calculator-ii/submissions/
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
                
        # perform div/mult operations
        # as much as possible from top
        # of the stack
        def divOrMult():
            while len(stack) > 2:
                a = stack[-3]
                op = stack[-2]
                b = stack[-1]

                if op == "*":
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.append(a * b)
                elif op == "/":
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.append(a // b)
                else:
                    break
        
        for c in s:
            if c == " ":
                continue
                
            elif c.isnumeric():
                if stack and type(stack[-1]) == int:
                    # top of stack is a number
                    # current char is also a number
                    # we will combine them into a single
                    # number
                    stack[-1] *= 10
                    
                    if stack[-1] < 0:    
                        stack[-1] -= int(c)
                    else:
                        stack[-1] += int(c)
                else:
                    # otherwise, add it to the top
                    # of stack
                    stack.append(int(c))
            
            else:
                # c is an operator
                # we will resolve any div or mult at
                # the top of the stack
                divOrMult()
                stack.append(c)

        # we also attempt to div or mult one more time after looping
        # through the string once
        #
        # this is to handle the edge case where a mult/div occurs as
        # the last operation.
        divOrMult()
                
        res = 0
        op = "+"
        for i in range(len(stack)):
            val = stack[i]
            if type(val) != int:
                op = val
            else:
                # at this point, we shouldn't have any more
                # div/mult operations
                if op == "-":
                    res -= val
                elif op == "+":
                    res += val
                else:
                    raise Exception("illegal operation: {}".format(op))
        return res
