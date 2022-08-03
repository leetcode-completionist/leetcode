import sortedcontainers

class MyCalendar:

    def __init__(self):
        # Initialize array with a "floor" event
        # and a "ceiling" event to avoid boundary edge cases
        self.events = sortedcontainers.SortedList([
            (float("-inf"), float("-inf")),
            (float("inf"), float("inf"))
        ])

    def book(self, start: int, end: int) -> bool:
        idx = self.events.bisect_left((start, end))
        
        next_event_start, _ = self.events[idx]
        if next_event_start < end:
            # this booking won't end on time for 
            # an existing next event
            return False
        
        _, prev_event_end = self.events[idx - 1]
        if prev_event_end > start:
            # this booking will start before
            # an existing prev event ends
            return False
        
        # no event conflicts
        self.events.add((start, end))
        return True
            

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
