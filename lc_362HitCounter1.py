class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        (1, 300)
        [1,2,3,4,..., 300]
        
        return len(lst)
        """
        self.l = deque([])

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        self.l.append(timestamp)
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.l and self.l[0] <= timestamp - 300:
            self.l.popleft()
      
        return len(self.l)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)