import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.i = 1 # starting point
        self.popped = set()
        self.added_back = []

    def popSmallest(self) -> int:
        while self.added_back:
            res = heapq.heappop(self.added_back)
            if res not in self.popped:
                self.popped.add(res)
                return res
        res = self.i
        self.i += 1
        self.popped.add(res)
        return res

    def addBack(self, num: int) -> None:
        if num < self.i and num in self.popped:
            self.popped.remove(num)
            heapq.heappush(self.added_back, num)
