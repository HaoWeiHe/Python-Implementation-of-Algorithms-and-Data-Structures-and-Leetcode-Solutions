class MedianFinder(object):
    """
    [1,2,3,4]
     4/2 = 2 (cur, cur - 1)
    [1,2,3]
    3/2 = 1 (cur)
    BST, to lst
    if len(lst) is even, return avg(mid, mid-1)
    else: return mid
    
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        #exist g(m) > 0 s.t. x>=m else <=0
        def bfs(target):
            l, r = 0, len(self.lst) #[1:r)
            while l < r:
                mid = (l+r) / 2 
                if self.lst[mid] > target : #g(mid) x >=m, g(x) > target
                    r = mid 
                else:
                    l  = mid + 1
            return l

        idx = bfs(num)

        self.lst =self.lst[:idx] +   [num] + self.lst[idx:]
        

    def findMedian(self):
        """
        :rtype: float
        """
        
        mid = len(self.lst)/2
        if len(self.lst)%2 == 0 :
            
            return (self.lst[mid] + self.lst[mid-1])/2.0
        else:
            
            return self.lst[mid]
        