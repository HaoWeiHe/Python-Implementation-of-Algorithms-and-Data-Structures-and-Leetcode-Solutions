"""
{user1: (start_station, checkin time), user2:(start_station, checkin time)}
{(start_station, end_Station):[time difference]} #by user1
"""

class UndergroundSystem(object):

    def __init__(self):
        self.userInfo = {}
        self.stationsInfo = collections.defaultdict(list)
    
    def checkIn(self, id, stationName, t):

        self.userInfo[id] = (stationName, t)

    def checkOut(self, id, end_station, t):
        start_staton, start_time = self.userInfo[id]
        self.stationsInfo[(start_staton,end_station)].append(t-start_time)
        

    def getAverageTime(self, start_staton, end_station):
        res = self.stationsInfo[(start_staton,end_station)]
        return sum(res)/float(len(res))
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)