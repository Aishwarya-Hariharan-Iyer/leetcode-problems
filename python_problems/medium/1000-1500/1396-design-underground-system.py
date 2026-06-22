from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.customer_status = dict() # (customer) -> (checked_in, tstart)
        self.travelling_times = defaultdict(list) # (start, end) -> [t1, t2, ....]
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer_status[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        customer_start_station, start_time = self.customer_status[id]
        travel_time = t - start_time
        self.travelling_times[(customer_start_station, stationName)].append(travel_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        t = self.travelling_times[(startStation, endStation)]
        return sum(t)/len(t)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)