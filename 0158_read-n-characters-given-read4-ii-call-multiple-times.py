# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    
    def __init__(self) -> None:
        self.buffer = [""] * 4
        
        # start and end pointers that indicate
        # buffer cells with valid data
        self.buffer_start = -1
        self.buffer_end = 0
    
    def read(self, buf: List[str], n: int) -> int:
        buf_idx = 0
        
        # check if we have anything in buffer first
        if self.buffer_start > -1:
            while n and self.buffer_start < self.buffer_end:
                buf[buf_idx] = self.buffer[self.buffer_start]
                buf_idx += 1
                self.buffer_start += 1
                n -= 1
        
        # while we still need more data, call read4
        while n:
            count = read4(self.buffer)
            if not count:
                return buf_idx
            
            # set the buffer
            self.buffer_start = 0
            self.buffer_end = count
        
            while n and self.buffer_start < self.buffer_end:
                buf[buf_idx] = self.buffer[self.buffer_start]
                buf_idx += 1
                self.buffer_start += 1
                n -= 1
            
        return buf_idx
