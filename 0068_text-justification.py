class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        res = []
        
        # create a reusable buffer
        buffer = Buffer(max_width)
        for word in words:
            if len(word) + buffer.char_count + len(buffer.buf)> max_width:
                # current word doesn't fit in buffer
                # so we flush buffer to new line
                res.append(buffer.flush())
            # add word to buffer
            buffer.add(word)
        
        # flush last line to results
        res.append(buffer.flush(end=True))

        return res
    
class Buffer:
    """
    A buffer to keeps track of a list of words and char_count.
    
    It will flush its content to a text-justified string of max_width.
    """
    def __init__(self, max_width: int) -> None:
        self.max_width = max_width
        self.char_count = 0
        self.buf = []
    
    
    def add(self, word: str) -> None:
        self.char_count += len(word)
        self.buf.append(word)
        
        
    def flush(self, end: bool = False) -> str:
        # number of spaces allowed
        space_count = self.max_width - self.char_count
        
        if len(self.buf) == 1:
            # one word with all spaces after it
            self.buf[0] += " " * space_count
        elif end:
            # we are building the last line:
            # add a single space for 0 ... n-1
            for i in range(0, len(self.buf) - 1):
                self.buf[i] += " "
            # then add remaining spaces to the last word
            self.buf[-1] += " " * (space_count - (len(self.buf) - 1))
        else:
            # evenly distribute spaces for 0 ... n-1, with no spaces
            # added to nth word
            for i in range(space_count):
                self.buf[i % (len(self.buf) - 1)] += " "
        
        res = "".join(self.buf)
        
        # reset buffer
        self.char_count = 0
        self.buf = []
        
        return res
