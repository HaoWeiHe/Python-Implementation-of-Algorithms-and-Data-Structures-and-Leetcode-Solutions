from heapq import heappush as push, heappop as pop

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []
        

    def addNum(self, x):
        """
        :type num: int
        :rtype: None
        """
        if len(self.right) == len(self.left):
            push(self.right, x)
            _min = pop(self.right)
            push(self.left, -_min)
        else:
            push(self.left, - x )
            _max = pop(self.left)
            push(self.right, -1*_max) 
        
    def findMedian(self):
        """
        :rtype: float
        """
        
        if len(self.right) == len(self.left):
            return (self.right[0] -  self.left[0])/2.0
        else:
            return -self.left[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()