# https://leetcode.com/problems/zigzag-iterator/
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        # we can put arbitrary number of vecs here
        self.vecs = deque()
        
        if v1:
            self.vecs.append((v1, 0))
        if v2:
            self.vecs.append((v2, 0))

            
    def next(self) -> int:
        v, i = self.vecs.popleft()
        ret = v[i]
        i += 1
        if i < len(v):
            self.vecs.append((v, i))
        
        return ret

    
    def hasNext(self) -> bool:
        return len(self.vecs)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
