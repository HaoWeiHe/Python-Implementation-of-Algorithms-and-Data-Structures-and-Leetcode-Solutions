class UndergroundSystem(object):

    def __init__(self):
       #(A,B), acc = 0, num = 0 
       #{45: A, starttime}
        self.station = {}
        self.cust = {}
        
    def checkIn(self, id, stationName, t):
        self.cust[id] = [stationName, t]
        
    def checkOut(self, id, stationName, t):
        fromStation, start_time = self.cust[id]
        tup = (fromStation,stationName)
        if tup in self.station:
            acc, num = self.station[tup]
            self.station[tup] = [acc + (t-start_time), num + 1]
        else:
            self.station[tup] = [t-start_time,1.0]
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
      
        acc, num =self.station[(startStation, endStation)]
        return acc/num if num != 0 else acc
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)