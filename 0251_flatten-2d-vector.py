# https://leetcode.com/problems/flatten-2d-vector/
class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.i = 0
        self.j = 0
        self.vec = vec

        
    def goToNext(self) -> None:
        """
        Determine if we are at the end of an inner list.
        If no, we will do nothing.
        
        If so, we will go to the next list in the 2D vec.
        
        We will keep moving if we encounter empty lists
        until we encounter an non-empty list or we are at
        the end of vec.
        """
        while self.i < len(self.vec) and self.j == len(self.vec[self.i]):
            # handles nested empty lists
            # move our pointer to the next available number
            self.i += 1
            self.j = 0
    
        
    def next(self) -> int:
        # move our pointer to the next number
        self.goToNext()
        
        res = self.vec[self.i][self.j]
        
        self.j += 1

        return res


    def hasNext(self) -> bool:
        # see if we need to move our pointer up to the next
        # number
        self.goToNext()
        
        return self.i < len(self.vec)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
