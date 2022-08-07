class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""

        while columnNumber:
            # decrease by 1 for zero-index
            columnNumber -= 1
            
            # start from the smallest digits
            # of this base26 number
            n = columnNumber % 26
            
            # add to the front of the string
            # because we are operating on
            # higher and higher base26 digits
            res = chr(n + ord("A")) + res
            
            # divide by 26 to move onto the next
            # base26 digits
            columnNumber //= 26

        return res
