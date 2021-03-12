class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 0           here
        
        self.time = collections.defaultdict(int)
    def hit(self, t):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        
        self.time[t] += 1
    def getHits(self, t):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        res = 0 
        
        for i in range(max(0, t-300+1), t+1):
            res += self.time[i]
        return res
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)