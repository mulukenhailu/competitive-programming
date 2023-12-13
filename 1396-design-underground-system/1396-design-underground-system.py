class UndergroundSystem:

    def __init__(self):
        self.start = {}
        self.counter={}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, ptime = self.start[id]
        self.start[id][0] = (start, stationName)
        self.start[id][1] = t - ptime
        
        if self.start[id][0] in self.counter:
            total_time, count = self.counter[self.start[id][0]]
            self.counter[self.start[id][0]] = (total_time + self.start[id][1], count + 1)
        else:
            self.counter[ self.start[id][0]] = (self.start[id][1], 1)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        inout = (startStation, endStation)
        totava, count = self.counter[inout]
        return totava / count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id, stationName, t)
# obj.checkOut(id, stationName, t)
# param_3 = obj.getAverageTime(startStation, endStation)
