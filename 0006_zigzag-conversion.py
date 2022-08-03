class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = {}
        
        is_down = True
        row_index = 1
        for c in s:
            if row_index not in rows:
                rows[row_index] = []
            rows[row_index].append(c)
            
            if is_down:
                if row_index < numRows:
                    row_index += 1
                else:
                    row_index -= 1
                    is_down = False
            else:
                if row_index > 1:
                    row_index -= 1
                else:
                    row_index += 1
                    is_down = True
        
        res = ""
        for i in range(1, len(rows.keys()) + 1):
            res += "".join(rows[i])
            
        return res
