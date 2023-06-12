class Solution:
    def smallestString(self, s: str) -> str:
        has_changed = False
        started = False
        
        out = []
        
        for c in s:
            if c == "a":
                out.append(c)
                started = False
            elif has_changed and started:
                out.append(chr(ord(c) - 1))
            elif not has_changed and not started:
                out.append(chr(ord(c) - 1))
                has_changed = True
                started = True
            else:
                out.append(c)
                    
        
        if has_changed:
            return "".join(out)
        
        out[len(out) - 1] = "z"
        
        return "".join(out)
