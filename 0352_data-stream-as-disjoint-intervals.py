from sortedcontainers import SortedList

class SummaryRanges:

    
    def __init__(self):
        self.ranges = SortedList()

        
    def addNum(self, value: int) -> None:
        # attempt to insert value into an existing range
        # where 'start' is largest up to value.
        insert = self.ranges.bisect_left([value, -1])    
        if insert > 0:
            # left neighbor possible
            left_neighbor = self.ranges[insert - 1]
            if left_neighbor[1] >= (value - 1):
                # range merge
                left_neighbor[1] = max(left_neighbor[1], value)
                insert -= 1
            else:
                # new range by itself
                self.ranges.add([value, value])
        else:
            # no left neighbor possible
            # new range by itself
            self.ranges.add([value, value])
        
        # try merge right neighbor
        if insert < len(self.ranges) - 1:
            # right neighbor possible
            right_neighbor = self.ranges[insert + 1]
            if right_neighbor[0] <= (value + 1):
                # range merge
                self.ranges[insert][1] = max(
                    self.ranges[insert][1], right_neighbor[1])
                # remove right neighbor
                self.ranges.pop(insert + 1)
        

    def getIntervals(self) -> List[List[int]]:
        return self.ranges


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
