# https://leetcode.com/problems/design-circular-queue/
class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [-1] * k
        self.tail_p = 0
        self.insert_p = 0
        self.empty = True
        
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.arr[self.insert_p] = value
        self.insert_p = (self.insert_p + 1) % len(self.arr)
        self.empty = False
        
        return True

    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.arr[self.tail_p] = -1
        self.tail_p = (self.tail_p + 1) % len(self.arr)
        if self.tail_p == self.insert_p:
            self.empty = True
        
        return True

    
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.tail_p]
        
    
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.insert_p - 1]

    
    def isEmpty(self) -> bool:
        return self.empty

    
    def isFull(self) -> bool:
        return not self.isEmpty() and self.tail_p == self.insert_p
        

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
