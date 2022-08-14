class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        
        for c in s:
            if c == " ":
                # skip spaces
                continue
            
            elif c.isnumeric():
                # current char is a number
                if (not stack or
                    stack[-1] == "(" or
                    stack[-1] == "+"):
                    # there is no previous number to combine
                    # with, we append directly
                    stack.append(int(c))
                    
                elif stack[-1] == "-":
                    # update previous cell to be a negative
                    # number
                    stack[-1] = -int(c)
                    
                else:
                    # add to previous number
                    stack[-1] *= 10
                    
                    if stack[-1] < 0:
                        # if prev number is negative
                        # we want to subtract
                        stack[-1] -= int(c)
                    else:
                        # otherwise, we add
                        stack[-1] += int(c)
            
            elif c == "(":
                # no special handling needed, we append to list
                stack.append(c)
            
            elif c == "+":
                # if there are less than 3 elements
                # we don't have prior additions to perform yet
                if len(stack) < 3:
                    stack.append(c)
                
                else:
                    a = stack[-3]
                    sign = stack[-2]
                    b = stack[-1]
                    
                    if type(a) == int and type(b) == int and sign == "+":
                        # check that the last three elements are
                        # an addition operation
                        a = stack.pop()
                        sign = stack.pop()
                        b = stack.pop()
                        stack.append(a + b)
                
                    # we always add the plus sign
                    stack.append(c)
            
            elif c == ")":
                # we need to combine all values up to a
                # left parenthesis.
                n_val = 0
                while stack[-1] != "(":
                    val = stack.pop()
                    if type(val) == int:
                        # ignore all non numbers
                        n_val += val 
                    
                # evict the left parenthesis
                stack.pop()
                
                if stack and stack[-1] == "-":
                    # this is an edge case where
                    # a negative sign precedes a left
                    # parenthesis
                    #
                    # we set stack's last value to be
                    # the negative number
                    stack[-1] = -n_val
                else:
                    # otherwise, we add number to stack
                    stack.append(n_val)
                
            elif c == "-":
                # add negative sign directly to the stack
                stack.append(c)
        
        # we will sum up remaining elements that are integers
        return sum([i if type(i) == int else 0 for i in stack])
                
