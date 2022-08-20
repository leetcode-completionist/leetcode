# https://leetcode.com/problems/encode-and-decode-strings/
class Codec:
    # Special character used to delimit elements in an array
    DELIMITER = ','
    
    # Special character used to escape reserved chars
    ESCAPE = '\\'
    
    # Collection of special characters
    RESERVED = '\",' + ESCAPE
    
    
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = []
        
        for s in strs:
            out = ''
            for c in s:
                if c in Codec.RESERVED:
                    out += Codec.ESCAPE + c
                else:
                    out += c
            encoded.append(out)

        return Codec.DELIMITER.join(encoded)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        
        buf = ''
        i = 0
        while i < len(s):
            if s[i] == Codec.DELIMITER:
                res.append(buf)
                buf = ''
                i += 1
                
            elif s[i] == Codec.ESCAPE:
                buf += s[i + 1]
                i += 2
                
            else:
                buf += s[i]
                i += 1
        
        res.append(buf)
        
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
