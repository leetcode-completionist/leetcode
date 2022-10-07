# https://leetcode.com/problems/my-calendar-iii/
from sortedcontainers import SortedList

class MyCalendarThree:

    def __init__(self):
        self.calendar = SortedList([[0,0]])
        self.max_k = 0


    def insert(self, booking: int) -> None:
        i = self.calendar.bisect_left([booking, 0])
        if i == len(self.calendar) or self.calendar[i][0] != booking:
            self.calendar.add([booking, self.calendar[i - 1][1]])


    def book(self, start: int, end: int) -> int:
        # Insert initial values for start/end.
        #
        # It uses the value of the point immediately to the
        # left for initial state.
        self.insert(start)
        self.insert(end)

        # For each interval within our range, increase the counter
        # Compare against our existing max_k for our final result
        minimum = [start, 0]
        maximum = [end, 0]
        inclusive = (True, False)

        for interval in self.calendar.irange(minimum, maximum, inclusive):
            interval[1] += 1
            self.max_k = max(self.max_k, interval[1])

        return self.max_k
