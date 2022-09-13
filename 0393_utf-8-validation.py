# https://leetcode.com/problems/utf-8-validation/
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i, n = 0, len(data)
        
        while i < n:
            if data[i] & (1 << 7) == 0:
                # 1-byte character
                i += 1
                continue
            
            # determine number of bytes
            n_bytes = 0
            octet = data[i]
            for j in range(7, 1, -1):
                # check from most to least significant bit
                # and count leading 1's
                if octet & (1 << j) != 0:
                    n_bytes += 1
                else:
                    break

            if n_bytes < 2 or n_bytes > 4:
                # invalid UTF8 length
                return False
            
            # check the next n_bytes - 1
            for _ in range(n_bytes - 1):
                i += 1
                if i == n:
                    # not enough bytes left
                    return False
                
                octet = data[i]
                if octet & (1 << 7) == 0 or octet & (1 << 6) != 0:
                    # most significant 2 bits must be 10
                    # to be a continuation byte
                    return False
                
            # move onto the next octet
            i += 1

        return True
