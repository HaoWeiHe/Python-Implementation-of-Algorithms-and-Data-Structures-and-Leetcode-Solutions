class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.lst = deque([])

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.lst.append(val)
        if len(self.lst) > self.size:
            self.lst.popleft()
        
        return sum(self.lst) / float(len(self.lst))
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)