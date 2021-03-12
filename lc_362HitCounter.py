class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()

    def hit(self, t):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        self.q.append(t)
        

    def getHits(self, t):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        lower = t - 300 + 1
        while self.q and self.q[0] < lower:
            self.q.popleft()
        return len(self.q)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)