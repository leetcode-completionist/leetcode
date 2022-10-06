# https://leetcode.com/problems/time-based-key-value-store/
class TimeMap:

    def __init__(self):
        # timestamp in test cases are suppose
        # to be strictly increasing, so we use a list
        #
        # if timestamp is not strictly increasing,
        # we need a SortedList
        self.m = defaultdict(list)

        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((timestamp, value))

        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""

        vals = self.m[key]

        i = bisect.bisect_left(vals, (timestamp, ""))

        if i == len(vals):
            return vals[-1][-1]
        
        if vals[i][0] == timestamp:
            return vals[i][-1]

        if i == 0:
            return ""

        return vals[i - 1][-1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
