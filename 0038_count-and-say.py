class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for i in range(1, n):
            res = self.count(res)
        return res

    def count(self, s: str) -> str:
        res = ""
        last_c = None
        last_c_count = 0
        for c in s:
            if not last_c:
                last_c = c
                last_c_count = 1
            elif c == last_c:
                last_c_count += 1
            else:
                res += str(last_c_count) + last_c
                last_c = c
                last_c_count = 1
        
        if last_c:
            res += str(last_c_count) + last_c
        
        return res
