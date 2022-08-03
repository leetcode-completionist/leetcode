class Solution:
    def addBinary(self, a: str, b: str) -> str:
        while len(a) < len(b):
            a = "0" + a
        while len(b) < len(a):
            b = "0" + b
            
        res = ""

        n = len(a)
        carry = 0
        for i in range(1, n + 1):
            # start from the end
            bit1 = a[n - i]
            bit2 = b[n - i]
            
            # sum up all the bits including carry
            val = ((ord(bit1) - ord("0")) +
                   (ord(bit2) - ord("0")) +
                   carry)
            
            # we only have 4 possible outcomes
            match val:
                case 0:
                    res = "0" + res
                    carry = 0
                case 1:
                    res = "1" + res
                    carry = 0
                case 2:
                    res = "0" + res
                    carry = 1
                case 3:
                    res = "1" + res
                    carry = 1
            
        if carry:
            res = "1" + res
        
        return res
