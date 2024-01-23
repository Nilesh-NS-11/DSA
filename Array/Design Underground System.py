"""

Design Underground System

An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.

Implement the UndergroundSystem class:

void checkIn(int id, string stationName, int t)
A customer with a card ID equal to id, checks in at the station stationName at time t.
A customer can only be checked into one place at a time.
void checkOut(int id, string stationName, int t)
A customer with a card ID equal to id, checks out from the station stationName at time t.
double getAverageTime(string startStation, string endStation)
Returns the average time it takes to travel from startStation to endStation.
The average time is computed from all the previous traveling times from startStation to endStation that happened directly, meaning a check in at startStation followed by a check out from endStation.
The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation to startStation.
There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.
You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in at time t1 then checks out at time t2, then t1 < t2. All events happen in chronological order.

 

Example 1:

Input
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

Output
[null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]

"""

class UndergroundSystem:

    def __init__(self):
        self.avgMap = {}
        self.checkInMap = {}
        
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName,t)
        
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, check_in_time = self.checkInMap.pop(id)
        travel = (start_station,stationName)
        travel_time = t - check_in_time

        if travel in self.avgMap:
            total_time, count = self.avgMap[travel]
            self.avgMap[travel] = (total_time + travel_time,count+1)
        else:
            self.avgMap[travel] = (travel_time,1)

        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel = (startStation,endStation)
        total_time,count = self.avgMap[travel]
        return total_time/count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)