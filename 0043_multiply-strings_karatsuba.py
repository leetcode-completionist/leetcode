class Solution:
    """
    This is an implementation of the Karatsuba multiplication algorithm.

    Let's compare elementary vs. Karatsuba multiplication with the
    following example:

         12
       x 34
       ----
        408

    Elementary multiplication would result in us calculating

        2*4 + 1*4*10^1 + 2*3*10^1 + 1*3*10^2 = 408
        ---   ===        ===        ---

    There are four multiplications (underlined) or 2^2 or O(n^2).

    Karatsuba multiplication (https://en.wikipedia.org/wiki/Karatsuba_algorithm)
    would result in us calculating first:

        1*3 = 3 and 2*4 = 8

    Then we calculate:

        (1+2)(3+4) = 21

    Then we calculate:

        (1+2)(3+4) - 1*3 - 2*4 = 10

    Then we sum everything up with their correct base:

        3*10^2 + 10*10^1 + 8 = 408

    So far, we've performed only three multiplications.
    We can always pad zeroes for the correct base.

    The reason why this works is because of (1+2)(3+4):

        (1+2)(3+4) = 2*4 + 1*4 + 2*3 + 1*3
                     ---   =========   ---

    1. Notice that these multiplications matches our elementary approach
    2. Notice that 1*4 and 2*3 shares the same base (10^1) in our elementary approach

    Instead of calculating 1*4 and 2*3 directly, we can reuse 1*3 and 2*4 and
    make one more multiplication (1+2)(3+4):

        (1+2)(3+4) - 2*4 - 1*3 = 1*4 + 2*3

    The above can be used to recursively build up multiplication between two integers.
    One way we can simplify our implementation is to left pad the shorter number with zeroes
    so that both numbers are of the same string length.
    
    The given the following:
    
         ab
       x cd
       
    And n == len(ab) == len(cd)
    
    The recurrance formula is:
    
        karatsuba(ab, cd) = 10^n*ac + 10^(n/2)*karatsuba(a+b, c+d) - ac - bd
        
    It has a runtime complexity of O(n^log2(3)).

    Resources:
    - https://youtu.be/JCbZayFr9RE
    - https://youtu.be/cCKOl5li6YM
    """
    @cache
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        elif num1 == "1":
            return num2
        elif num2 == "1": 
            return num1
        
        num1, num2 = self.padLeft(num1, num2)

        if len(num1) == 1 and len(num2) == 1:
            # This is the only time we multiply
            return str(self.getDigit(num1) * self.getDigit(num2))

        mid = len(num1) // 2

        # Assume numbers are 1234, 5678
        # a = 12, b = 34
        # c = 56, d = 78
        a = num1[:len(num1) - mid]
        b = num1[len(num1) - mid:]
        c = num2[:len(num2) - mid]
        d = num2[len(num2) - mid:]

        ac = self.multiply(a, c)
        bd = self.multiply(b, d)

        # (a+b)(c+d) - ac - bd = ad + bc
        ad_bc = self.subtract(
            self.subtract(
                self.multiply(
                    self.add(a, b),
                    self.add(c, d)), ac), bd)

        # pad the numbers with appropriate zeroes to the right
        ac = self.padRight(ac, mid + mid) # 10**2n
        ad_bc = self.padRight(ad_bc, mid) # 10**n
        
        # sum up all the terms for desired product
        res = self.add(self.add(ac, ad_bc), bd)
        
        if len(res) == 1:
            return res
        
        # remove unnecessary zeroes to the left
        while len(res) and res[0] == "0":
            res = res[1:]
        
        return res
    

    def padLeft(self, x: str, y: str) -> (str, str):
        # left pad the shorter number with zeroes
        # until both are the same length
        while len(x) < len(y):
            x = "0" + x
        while len(y) < len(x):
            y = "0" + y
        return x, y
    
    
    def padRight(self, num: str, n: int) -> str:
        if num != "0":
            for i in range(n):
                num += "0"
        return num


    def add(self, x: str, y: str) -> str:
        x, y = self.padLeft(x, y)
        res = ""
        carry = 0
        for i in range(len(x) - 1, -1, -1):
            s = self.getDigit(x[i]) + self.getDigit(y[i]) + carry
            c = s % 10
            carry = 0 if s == c else 1
            res = str(c) + res
        if carry:
            res = "1" + res
        return res


    def subtract(self, larger: str, smaller: str) -> str:
        # we can always assume that we are subtracting the smaller number
        # from the larger number
        larger, smaller = self.padLeft(larger, smaller)
        res = ""
        borrow = 0
        for i in range(len(larger) - 1, -1, -1):
            c = self.getDigit(larger[i]) - self.getDigit(smaller[i]) - borrow
            borrow = 0
            if c >= 0:
                res = str(c) + res
            else:
                c += 10
                res = str(c) + res
                borrow = 1
        return res
        
    
    def getDigit(self, n: str) -> int:
        return ord(n) - ord("0")
