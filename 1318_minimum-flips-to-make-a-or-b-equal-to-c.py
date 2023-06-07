class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a_binary = format(a, '#032b')
        b_binary = format(b, '#032b')
        c_binary = format(c, '#032b')
        
        flips = 0
        
        # ignore '0b' prefix
        for i in range(2, len(a_binary)):
            if c_binary[i] == '0':
                if a_binary[i] == '1':
                    flips += 1
                if b_binary[i] == '1':
                    flips += 1
            else:
                # '1'
                if a_binary[i] == '0' and b_binary[i] == '0':
                    flips += 1
                
        return flips
