class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP and self.is_ipv4(queryIP):
            return "IPv4"
        
        if ":" in queryIP and self.is_ipv6(queryIP):
            return "IPv6"
        
        return "Neither"
    
    
    def is_ipv4(self, queryIP: str) -> bool:
        nums = queryIP.split(".")

        if len(nums) != 4:
            return False
            
        for num in nums:
            if not num.isdigit():
                return False
            
            if num == "0":
                continue
                
            if num[0] == "0":
                return False
            
            num = int(num)
            if num < 0 or num > 255:
                return False
        
        return True
    
    
    def is_ipv6(self, queryIP: str) -> bool:
        parts = queryIP.split(":")
        
        if len(parts) != 8:
            return False
        
        for part in parts:
            n = len(part)
            
            if n < 1 or n > 4:
                return False
            
            for c in part:
                code = ord(c)
                
                if ord("0") <= code <= ord("9"):
                    continue
                if ord("a") <= code <= ord("f"):
                    continue
                if ord("A") <= code <= ord("F"):
                    continue
                
                return False
        
        return True
