class StationEntry:
    
    def __init__(self):
        self.total_time = 0
        self.count = 0
        
    def add(self, t: int):
        self.total_time += t
        self.count += 1
        
    def get_average(self) -> float:
        return self.total_time / self.count

    
class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.station_times = {}

    def checkIn(self, id: int, station: str, t: int) -> None:
        self.customers[id] = (station, t)

    def checkOut(self, id: int, end: str, end_time: int) -> None:
        start, start_time = self.customers[id]
        del self.customers[id]
        
        if start not in self.station_times:
            self.station_times[start] = {}
        if end not in self.station_times[start]:
            self.station_times[start][end] = StationEntry()
        
        self.station_times[start][end].add(end_time - start_time)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.station_times[startStation][endStation].get_average()


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
