import itertools
import heapq

class MinStack:

    INVALID_UID = -1
    
    def __init__(self):
        self.stack = []
        self.heap = []
        self.counter = itertools.count()


    def push(self, val: int) -> None:
        node = [val, next(self.counter)]
        self.stack.append(node)
        heapq.heappush(self.heap, node)
        

    def pop(self) -> None:
        node = self.stack.pop()
        node[-1] = MinStack.INVALID_UID        
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        while self.heap:
            if self.heap[0][-1] == MinStack.INVALID_UID:
                heapq.heappop(self.heap)
            else:
                break
        
        return self.heap[0][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
