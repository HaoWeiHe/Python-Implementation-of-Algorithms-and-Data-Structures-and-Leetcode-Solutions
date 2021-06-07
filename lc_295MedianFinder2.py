from heapq import heappop as hpop, heappush as hpush
class MedianFinder(object):
    """
        3,5,1,2
     minheap   max heap
        3       2
        5       1 
                
insert:1
        3       5
                    1
        5       3 
                    1
insert 2:
          2       3 
       5             1
    if lg ==, insert to maxheap and cmp two top
    if lg!=, insert to minheap and cmp two top
        
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minh = []
        self.maxh = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.maxh:
            hpush(self.maxh, -num)
            return 
        
        if len(self.minh) == len(self.maxh):
            hpush(self.maxh, -num)
        else:
            hpush(self.minh, num)
        """
        minheap   max heap
        1          3 
                     2
        
        """     
        top_min, top_max = hpop(self.maxh)*-1, hpop(self.minh)
        hpush(self.maxh, -1*min(top_min, top_max))
        hpush(self.minh, max(top_min, top_max))
        return

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minh) == len(self.maxh):
            return (-1*self.maxh[0] + self.minh[0])/ 2.0
      
        return -1*self.maxh[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()