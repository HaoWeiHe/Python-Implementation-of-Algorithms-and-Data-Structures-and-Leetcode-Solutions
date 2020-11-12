

class MedianFinder(object):

    def __init__(self):
        """
        small half = maxheap
        large half = minheap
        select : to point which bucket shoule be increase new ele
        
        """
        self.small = []
        self.large = []
        
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """

    def addNum(self, num):

        if len(self.small) == len(self.large):
            heappush(self.small, -heappushpop(self.large, num))
        else:
            heappush(self.large, -heappushpop(self.small, -num))
        
    def findMedian(self):
        """
        :rtype: float
        """
        
        if len(self.small) == len(self.large):
            return float(-self.small[0] + self.large[0])/2.0
        return -self.small[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()